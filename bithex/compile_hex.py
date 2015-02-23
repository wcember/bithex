import re

from constants import *

class InvalidHexError(Exception):
    '''Raised by compile_hex, classify_hex if the input doesn't compile to
        valid Script.'''
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value + ' does not compile into valid Script'

def compile_hex(hex_string):
    '''Compile a hex string into Script.

    Args:
        hex_string: A string or unicode string that is the hex representation
            of a bitcoin script.

    Returns:
        str: A bitcoin script formatted as a string.

    Raises:
        InvalidHexError: Raised if the input hex_string doesn't compile to
            valid Script.
        TypeError: Raised if the input hex_string isn't a string.

    Examples:
        >>> compile_hex('aa206fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d619000000000087')
        'OP_HASH256 6fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d6190000000000 OP_EQUAL'
        >>> compile_hex('76a914a134408afa258a50ed7a1d9817f26b63cc9002cc88ac')
        'OP_DUP OP_HASH160 a134408afa258a50ed7a1d9817f26b63cc9002cc OP_EQUALVERIFY OP_CHECKSIG'
        >>> compile_hex('4104b0bd634234abbb1ba1e986e884185c61cf43e001f9137f23c2c409273eb16e6537a576782eba668a7ef8bd3b3cfb1edb7117ab65129b8a2e681f3c1e0908ef7bac')
        '04b0bd634234abbb1ba1e986e884185c61cf43e001f9137f23c2c409273eb16e6537a576782eba668a7ef8bd3b3cfb1edb7117ab65129b8a2e681f3c1e0908ef7b OP_CHECKSIG'
        >>> compile_hex('aa206fe28c0ab6f1b372c1a6a246ae63f74f931')
        InvalidHexError
    '''
    if not isinstance(hex_string, basestring):
        raise TypeError
    answer_list = []
    counter = 0
    end = len(hex_string)
    while counter < end:
        try:
            if hex_string[counter: counter + 2] in byte_dictionary:
                byte_length = int(byte_dictionary[hex_string[counter: counter + 2]], 16)
                counter += 2
                assert len(hex_string) >= counter + byte_length*2
                address = hex_string[counter: counter + byte_length*2]
                answer_list.append(address)
                counter += byte_length*2
            else:
                answer_list.append(hex_dictionary[hex_string[counter: counter + 2]])
                counter += 2
        except KeyError:
            raise InvalidHexError(hex_string)
        except AssertionError:
            raise InvalidHexError(hex_string)
    return ' '.join(answer_list)

def classify_hex(hex_string):
    '''Classify the transaction type of a hex string.

    Args:
        hex_string: A string or unicode string that is the hex representation
            of a bitcoin script.

    Returns:
        str: The transaction type of the hex string per
            https://bitcoin.org/en/developer-guide#standard-transactions.

    Raises:
        TypeError: Raised if the input hex_string isn't a string.
        InvalidHexError: Raised if the input hex_string doesn't compile to
            valid Script.

    Examples:
        >>> classify_hex_script('76a914a134408afa258a50ed7a1d9817f26b63cc9002cc88ac')
        'P2PKH'
        >>> classify_hex_script('aa206fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d619000000000087')
        'nonstandard transaction'
    '''
    if not isinstance(hex_string, basestring):
        raise TypeError
    script = compile_hex(hex_string)
    return classify_script(script)

def classify_script(script):
    '''Classify the transaction type of a script.

    Args:
        script: A bitcoin script.

    Returns:
        str: The transaction type of the hex string per
            https://bitcoin.org/en/developer-guide#standard-transactions.
            The following are the values that can be returned: 'P2PKH','P2SH',
            'Multisig', 'Pubkey', 'Null Data', 'nonstandard transaction'.

    Raises:
        TypeError: Raised if the input script isn't a string.

    Examples:
        >>> classify_script('OP_DUP OP_HASH160 a134408afa258a50ed7a1d9817f26b63cc9002cc OP_EQUALVERIFY OP_CHECKSIG')
        'P2PKH'
        >>> classify_script('OP_HASH160 54c557e07dde5bb6cb791c7a540e0a4796f5e97e OP_EQUAL')
        'P2SH'
        >>> classify_script('OP_HASH256 6fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d6190000000000 OP_EQUAL')
        'nonstandard transaction'
    '''
    if not isinstance(script, basestring):
        raise TypeError
    P2PKH_regex = re.compile('OP_DUP OP_HASH160 [abcdef0123456789]+ OP_EQUALVERIFY OP_CHECKSIG')
    P2SH_regex = re.compile('OP_HASH160 .* OP_EQUAL')
    multisig_regex = re.compile('OP_FALSE|OP_0|OP_TRUE [abcdef0123456789 ]+ OP_1|OP_2|OP_3|OP_4|OP_5 OP_CHECKMULTISIG')
    pubkey_regex = re.compile('[abcdef0123456789]+ OP_CHECKSIG')
    null_data_regex = re.compile('OP_RETURN [abcdef0123456789]+')
    regex_list = [
            P2PKH_regex,
            P2SH_regex,
            multisig_regex,
            pubkey_regex,
            null_data_regex,
    ]
    for index, regex in enumerate(regex_list):
        if regex.match(script):
            return standard_transactions[index]
    else:
        return 'nonstandard transaction'