import unittest

from compile_hex import compile_hex

class CompileHexTests(unittest.TestCase):
    def setUp(self):
        self.input_list = [
        'aa206fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d619000000000087',
        'aa01bb87',
        'aa4b11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111187',
        '76a9146aeb2b63d0ce62bb527f3ab8833eb95c29b97ab088ac',
        '76a914aafcc27a4a137976e1fbbed6314296b769793f2488ac',
        ]
        self.output_list = [
        'OP_HASH256 6fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d6190000000000 OP_EQUAL',
        'OP_HASH256 bb OP_EQUAL',
        'OP_HASH256 111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111 OP_EQUAL',
        'OP_DUP OP_HASH160 6aeb2b63d0ce62bb527f3ab8833eb95c29b97ab0 OP_EQUALVERIFY OP_CHECKSIG',
        'OP_DUP OP_HASH160 aafcc27a4a137976e1fbbed6314296b769793f24 OP_EQUALVERIFY OP_CHECKSIG'
        ]
    def test_hex_to_script(self):
        for input_str, output_str in zip(self.input_list, self.output_list):
            self.assertEqual(compile_hex(input_str), output_str)

if __name__ == '__main__':
    unittest.main()