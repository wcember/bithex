import unittest

from compile_hex import *

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
        self.assertEqual(classify_script('OP_HASH256 6fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d6190000000000 OP_EQUAL'),
                'P2PKH')
        self.assertEqual(classify_script('OP_DUP OP_HASH160 a134408afa258a50ed7a1d9817f26b63cc9002cc OP_EQUALVERIFY OP_CHECKSIG'),
                'P2SH')

class ClassifyHexTests(unittest.TestCase):
    def test_classify_hex_doc_string(self):
        self.assertEqual(classify_script('aa206fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d619000000000087'),
                'P2PKH')
        self.assertEqual(classify_script('76a914a134408afa258a50ed7a1d9817f26b63cc9002cc88ac'),
                'P2SH')

if __name__ == '__main__':
    unittest.main()