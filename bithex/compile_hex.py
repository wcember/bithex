import constants


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
        >>> compile_hex('aa106fe28c0ab6f1b372c1a6a246ae63f74f87')
        'OP_HASH256 6fe28c0ab6f1b372c1a6a246ae63f74f OP_EQUAL'
        >>> compile_hex('76a90a134408afa258a50ed7a188ac')
        'OP_DUP OP_HASH160 a134408afa258a50ed7a1 OP_EQUALVERIFY OP_CHECKSIG'
        >>> compile_hex('0504b0bd6342ac')
        '04b0bd6342 OP_CHECKSIG'
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
            next_word = hex_string[counter: counter + 2]
            next_word_int = int(next_word, 16)
            if 0 < next_word_int < 76:
                counter += 2
                assert len(hex_string) >= counter + next_word_int*2
                address = hex_string[counter: counter + next_word_int*2]
                answer_list.append(address)
                counter += next_word_int*2
            else:
                answer_list.append(constants.HEX_DICTIONARY[next_word])
                counter += 2
        except ValueError:
            raise InvalidHexError(hex_string)
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
        >>> classify_hex('76a914a134408afa258a50ed7a1d9817f26b63cc9002cc88ac')
        'P2PKH'
        >>> classify_hex('aa106fe28c0ab6f1b372c1a6a246ae63f74f87')
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
        >>> classify_script('OP_DUP OP_HASH160 a13 OP_EQUALVERIFY OP_CHECKSIG')
        'P2PKH'
        >>> classify_script('OP_HASH160 54c557e07dde5bb6cb791c7a540e OP_EQUAL')
        'P2SH'
        >>> classify_script('OP_HASH256 6fe28c0ab6f1b372c1a6a246ae63 OP_EQUAL')
        'nonstandard transaction'
    '''
    if not isinstance(script, basestring):
        raise TypeError
    for key, regex in constants.REGEX_PATTERNS.iteritems():
        if regex.match(script):
            return key
    else:
        return 'nonstandard transaction'
