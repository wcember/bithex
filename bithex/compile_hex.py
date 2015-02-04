from constants import *

class InvalidHexError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value + 'does not compile into valid Script'

def compile_hex(hex_string):
    '''Compile a hex string into Script.

    Args:
        hex_string: A string or unicode string that is the hex representation of
            a bitcoin script

    Returns: A bitcoin script formatted as a string

    Raises:
        InvalidHexError: An error occured if the input hex_string doesn't
            compile to valid Script.

    Example:
        >>> compile_hex('aa206fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d619000000000087')
        'OP_HASH256 6fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d6190000000000 OP_EQUAL'
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