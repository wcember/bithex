from constants import *

class InvalidHexError(Exception):
    pass

def compile_hex(hex_string):
    '''Compile a hex string into Script.

    Args:
      hex_string(str): A string or unicode string that is the hex
        representation of a bitcoin script

    Returns:
      str: bitcoin script

    Raises:
      FILL THIS OUT

    Example:
      FILL THIS OUT
    '''
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
            raise InvalidHexError
        except AssertionError:
            raise InvalidHexError
    return ' '.join(answer_list)