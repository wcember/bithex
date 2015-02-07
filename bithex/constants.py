hex_dictionary = {
    '00': 'OP_FALSE',
    '01': 'N/A',
    '02': 'N/A',
    '03': 'N/A',
    '04': 'N/A',
    '05': 'N/A',
    '06': 'N/A',
    '07': 'N/A',
    '08': 'N/A',
    '09': 'N/A',
    '0a': 'N/A',
    '0b': 'N/A',
    '0c': 'N/A',
    '0d': 'N/A',
    '0e': 'N/A',
    '0f': 'N/A',
    '10': 'N/A',
    '11': 'N/A',
    '12': 'N/A',
    '13': 'N/A',
    '14': 'N/A',
    '15': 'N/A',
    '16': 'N/A',
    '17': 'N/A',
    '18': 'N/A',
    '19': 'N/A',
    '1a': 'N/A',
    '1b': 'N/A',
    '1c': 'N/A',
    '1d': 'N/A',
    '1e': 'N/A',
    '1f': 'N/A',
    '20': 'N/A',
    '21': 'N/A',
    '22': 'N/A',
    '23': 'N/A',
    '24': 'N/A',
    '25': 'N/A',
    '26': 'N/A',
    '27': 'N/A',
    '28': 'N/A',
    '29': 'N/A',
    '2a': 'N/A',
    '2b': 'N/A',
    '2c': 'N/A',
    '2d': 'N/A',
    '2e': 'N/A',
    '2f': 'N/A',
    '30': 'N/A',
    '31': 'N/A',
    '32': 'N/A',
    '33': 'N/A',
    '34': 'N/A',
    '35': 'N/A',
    '36': 'N/A',
    '37': 'N/A',
    '38': 'N/A',
    '39': 'N/A',
    '3a': 'N/A',
    '3b': 'N/A',
    '3c': 'N/A',
    '3d': 'N/A',
    '3e': 'N/A',
    '3f': 'N/A',
    '40': 'N/A',
    '41': 'N/A',
    '42': 'N/A',
    '43': 'N/A',
    '44': 'N/A',
    '45': 'N/A',
    '46': 'N/A',
    '47': 'N/A',
    '48': 'N/A',
    '49': 'N/A',
    '4a': 'N/A',
    '4b': 'N/A',
    '4c': 'OP_PUSHDATA1',
    '4d': 'OP_PUSHDATA2',
    '4e': 'OP_PUSHDATA4',
    '4f': 'OP_1NEGATE',
    '51': 'OP_TRUE',
    '52': 'OP_2',
    '53': 'OP_3',
    '54': 'OP_4',
    '55': 'OP_5',
    '56': 'OP_6',
    '57': 'OP_7',
    '58': 'OP_8',
    '59': 'OP_9',
    '5a': 'OP_10',
    '5b': 'OP_11',
    '5c': 'OP_12',
    '5d': 'OP_13',
    '5e': 'OP_14',
    '5f': 'OP_15',
    '60': 'OP_16',
    '61': 'OP_NOP',
    '63': 'OP_IF',
    '64': 'OP_NOTIF',
    '67': 'OP_ELSE',
    '68': 'OP_ENDIF',
    '69': 'OP_VERIFY',
    '6a': 'OP_RETURN',
    '6b': 'OP_TOALTSTACK',
    '6c': 'OP_FROMALTSTACK',
    '73': 'OP_IFDUP',
    '74': 'OP_DEPTH',
    '75': 'OP_DROP',
    '76': 'OP_DUP',
    '77': 'OP_NIP',
    '78': 'OP_OVER',
    '79': 'OP_PICK',
    '7a': 'OP_ROLL',
    '7b': 'OP_ROT',
    '7c': 'OP_SWAP',
    '7d': 'OP_TUCK',
    '6d': 'OP_2DROP',
    '6e': 'OP_2DUP',
    '6f': 'OP_3DUP',
    '70': 'OP_2OVER',
    '71': 'OP_2ROT',
    '72': 'OP_2SWAP',
    '7e': 'OP_CAT',
    '7f': 'OP_SUBSTR',
    '80': 'OP_LEFT',
    '81': 'OP_RIGHT',
    '82': 'OP_SIZE',
    '83': 'OP_INVERT',
    '84': 'OP_AND',
    '85': 'OP_OR',
    '86': 'OP_XOR',
    '87': 'OP_EQUAL',
    '88': 'OP_EQUALVERIFY',
    '8b': 'OP_1ADD',
    '8c': 'OP_1SUB',
    '8d': 'OP_2MUL',
    '8e': 'OP_2DIV',
    '8f': 'OP_NEGATE',
    '90': 'OP_ABS',
    '91': 'OP_NOT',
    '92': 'OP_0NOTEQUAL',
    '93': 'OP_ADD',
    '94': 'OP_SUB',
    '95': 'OP_MUL',
    '96': 'OP_DIV',
    '97': 'OP_MOD',
    '98': 'OP_LSHIFT',
    '99': 'OP_RSHIFT',
    '9a': 'OP_BOOLAND',
    '9b': 'OP_BOOLOR',
    '9c': 'OP_NUMEQUAL',
    '9d': 'OP_NUMEQUALVERIFY',
    '9e': 'OP_NUMNOTEQUAL',
    '9f': 'OP_LESSTHAN',
    'a0': 'OP_GREATERTHAN',
    'a1': 'OP_LESSTHANOREQUAL',
    'a2': 'OP_GREATERTHANOREQUAL',
    'a3': 'OP_MIN',
    'a4': 'OP_MAX',
    'a5': 'OP_WITHIN',
    'a6': 'OP_RIPEMD160',
    'a7': 'OP_SHA1',
    'a8': 'OP_SHA256',
    'a9': 'OP_HASH160',
    'aa': 'OP_HASH256',
    'ab': 'OP_CODESEPARATOR',
    'ac': 'OP_CHECKSIG',
    'ad': 'OP_CHECKSIGVERIFY',
    'ae': 'OP_CHECKMULTISIG',
    'af': 'OP_CHECKMULTISIGVERIFY',
    'fd': 'OP_PUBKEYHASH',
    'fe': 'OP_PUBKEY',
    'ff': 'OP_INVALIDOPCODE',
    '50': 'OP_RESERVED',
    '62': 'OP_VER',
    '65': 'OP_VERIF',
    '66': 'OP_VERNOTIF',
    '89': 'OP_RESERVED1',
    '8a': 'OP_RESERVED2',
    'b0': 'OP_NOP0',
    'b1': 'OP_NOP1',
    'b2': 'OP_NOP2',
    'b3': 'OP_NOP3',
    'b4': 'OP_NOP4',
    'b5': 'OP_NOP5',
    'b6': 'OP_NOP6',
    'b7': 'OP_NOP7',
    'b8': 'OP_NOP8',
    'b9': 'OP_NOP9',
}

byte_dictionary = {
    '01' : '01',
    '02' : '02',
    '03' : '03',
    '04' : '04',
    '05' : '05',
    '06' : '06',
    '07' : '07',
    '08' : '08',
    '09' : '09',
    '0a' : '0a',
    '0b' : '0b',
    '0c' : '0c',
    '0d' : '0d',
    '0e' : '0e',
    '0f' : '0f',
    '10' : '10',
    '11' : '11',
    '12' : '12',
    '13' : '13',
    '14' : '14',
    '15' : '15',
    '16' : '16',
    '17' : '17',
    '18' : '18',
    '19' : '19',
    '1a' : '1a',
    '1b' : '1b',
    '1c' : '1c',
    '1d' : '1d',
    '1e' : '1e',
    '1f' : '1f',
    '20' : '20',
    '21' : '21',
    '22' : '22',
    '23' : '23',
    '24' : '24',
    '25' : '25',
    '26' : '26',
    '27' : '27',
    '28' : '28',
    '29' : '29',
    '2a' : '2a',
    '2b' : '2b',
    '2c' : '2c',
    '2d' : '2d',
    '2e' : '2e',
    '2f' : '2f',
    '30' : '30',
    '31' : '31',
    '32' : '32',
    '33' : '33',
    '34' : '34',
    '35' : '35',
    '36' : '36',
    '37' : '37',
    '38' : '38',
    '39' : '39',
    '3a' : '3a',
    '3b' : '3b',
    '3c' : '3c',
    '3d' : '3d',
    '3e' : '3e',
    '3f' : '3f',
    '40' : '40',
    '41' : '41',
    '42' : '42',
    '43' : '43',
    '44' : '44',
    '45' : '45',
    '46' : '46',
    '47' : '47',
    '48' : '48',
    '49' : '49',
    '4a' : '4a',
    '4b' : '4b',
    '4c': '01',
    '4d': '02',
    '4e': '04',
}

standard_transactions = [
    'P2PKH',
    'P2SH',
    'Multisig',
    'Pubkey',
    'Null Data',
]