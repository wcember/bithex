import unittest

from compile_hex import *
from constants import *

class CompileHexTests(unittest.TestCase):
    def test_hex_to_script(self):
        self.assertEqual(compile_hex('aa206fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d619000000000087'),
                'OP_HASH256 6fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d6190000000000 OP_EQUAL')
        self.assertEqual(compile_hex('aa01bb87'),
                'OP_HASH256 bb OP_EQUAL')
        self.assertEqual(compile_hex('aa4b11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111187'),
                'OP_HASH256 111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111 OP_EQUAL')
        self.assertEqual(compile_hex('76a9146aeb2b63d0ce62bb527f3ab8833eb95c29b97ab088ac'),
                'OP_DUP OP_HASH160 6aeb2b63d0ce62bb527f3ab8833eb95c29b97ab0 OP_EQUALVERIFY OP_CHECKSIG')
        self.assertEqual(compile_hex('76a914aafcc27a4a137976e1fbbed6314296b769793f2488ac'),
                'OP_DUP OP_HASH160 aafcc27a4a137976e1fbbed6314296b769793f24 OP_EQUALVERIFY OP_CHECKSIG')
        self.assertEqual(compile_hex('5121033d21e929938d33c12b895f37b4853a0087b587a9af87633c067e5ba7976501192102d94734eff2807d6b4f0e2993edd67cf41196875a4c96e6cee485604732e3f3ac2103a8367b923cdc0a79933dfb160969be6b7da0ee040e3b3e37ea498730fc0470a953ae'),
                        'OP_TRUE 033d21e929938d33c12b895f37b4853a0087b587a9af87633c067e5ba797650119 02d94734eff2807d6b4f0e2993edd67cf41196875a4c96e6cee485604732e3f3ac 03a8367b923cdc0a79933dfb160969be6b7da0ee040e3b3e37ea498730fc0470a9 OP_3 OP_CHECKMULTISIG')
        self.assertEqual(compile_hex(''), '')
    def test_hex_to_script_doc_string(self):
        self.assertEqual(compile_hex('aa206fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d619000000000087'),
                'OP_HASH256 6fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d6190000000000 OP_EQUAL')
        self.assertEqual(compile_hex('76a914a134408afa258a50ed7a1d9817f26b63cc9002cc88ac'),
                'OP_DUP OP_HASH160 a134408afa258a50ed7a1d9817f26b63cc9002cc OP_EQUALVERIFY OP_CHECKSIG')
        self.assertEqual(compile_hex('4104b0bd634234abbb1ba1e986e884185c61cf43e001f9137f23c2c409273eb16e6537a576782eba668a7ef8bd3b3cfb1edb7117ab65129b8a2e681f3c1e0908ef7bac'),
                '04b0bd634234abbb1ba1e986e884185c61cf43e001f9137f23c2c409273eb16e6537a576782eba668a7ef8bd3b3cfb1edb7117ab65129b8a2e681f3c1e0908ef7b OP_CHECKSIG')
        self.assertRaises(InvalidHexError, compile_hex, 'aa206fe28c0ab6f1b372c1a6a246ae63f74f931')
    def test_hex_to_script_unicode_input(self):
        self.assertEqual(compile_hex(u'aa01bb87'), 'OP_HASH256 bb OP_EQUAL')
    def test_InvalidHexError(self):
        self.assertRaises(InvalidHexError, compile_hex, 'invalid_string')
        self.assertRaises(InvalidHexError, compile_hex, ' ')
        self.assertRaises(InvalidHexError, compile_hex,
                'aa206fe28c0ab6f1b372c1a6a246ae63f74f931')
    def test_TypeError(self):
        self.assertRaises(TypeError, compile_hex, 0)
        self.assertRaises(TypeError, compile_hex, [])

class ClassifyScriptTests(unittest.TestCase):
    def test_classify_script_doc_string(self):
        self.assertEqual(classify_script('OP_DUP OP_HASH160 a134408afa258a50ed7a1d9817f26b63cc9002cc OP_EQUALVERIFY OP_CHECKSIG'),
                standard_transactions[0])
        self.assertEqual(classify_script('OP_HASH160 54c557e07dde5bb6cb791c7a540e0a4796f5e97e OP_EQUAL'),
                standard_transactions[1])
        self.assertEqual(classify_script('OP_0 a134408afa258a50ed7a1d9817f26b63cc9002cc a134408afa258a50ed7a1d9817f26b63cc9002cc OP_2 OP_CHECKMULTISIG'),
                standard_transactions[2])
        self.assertEqual(classify_script('04b0bd634234abbb1ba1e986e884185c61cf43e001f9137f23c2c409273eb16e6537a576782eba668a7ef8bd3b3cfb1edb7117ab65129b8a2e681f3c1e0908ef7b OP_CHECKSIG'),
                standard_transactions[3])
        self.assertEqual(classify_script('OP_RETURN abcdef123456'),
                standard_transactions[4])
        self.assertEqual(classify_script('OP_HASH256 6fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d6190000000000 OP_EQUAL'),
                'nonstandard transaction')
        self.assertEqual(classify_script('OP_TRUE 033d21e929938d33c12b895f37b4853a0087b587a9af87633c067e5ba797650119 02d94734eff2807d6b4f0e2993edd67cf41196875a4c96e6cee485604732e3f3ac 03a8367b923cdc0a79933dfb160969be6b7da0ee040e3b3e37ea498730fc0470a9 OP_3 OP_CHECKMULTISIG'),
                standard_transactions[2])
        self.assertEqual(classify_script('OP_FALSE 0 OP_1 OP_CHECKMULTISIG'),
                standard_transactions[2])
        self.assertEqual(classify_script('OP_FALSE 0 a OP_2 OP_CHECKMULTISIG'),
                standard_transactions[2])
        self.assertEqual(classify_script('OP_FALSE 0 a 0 OP_3 OP_CHECKMULTISIG'),
                standard_transactions[2])
        self.assertEqual(classify_script('OP_FALSE 0 a 0 2 OP_4 OP_CHECKMULTISIG'),
                standard_transactions[2])
        self.assertEqual(classify_script('OP_FALSE 0 a 0 2 b OP_5 OP_CHECKMULTISIG'),
                standard_transactions[2])

class ClassifyHexTests(unittest.TestCase):
    def test_classify_hex_doc_string(self):
        self.assertEqual(classify_hex('76a914a134408afa258a50ed7a1d9817f26b63cc9002cc88ac'),
                standard_transactions[0])
        self.assertEqual(classify_hex('aa106fe28c0ab6f1b372c1a6a246ae63f74f87'),
                'nonstandard transaction')

if __name__ == '__main__':
    unittest.main()