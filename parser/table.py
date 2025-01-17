table = {
    0: {
        'vtype': ('SHIFT', 4),
        None: ('REDUCE', 3),
        'CODE': ('GOTO', 1),
        'VDECL': ('GOTO', 2),
        'FDECL': ('GOTO', 3),
    },
    1: {
        None: ('ACCEPT', None),
    },
    2: {
        'vtype': ('SHIFT', 4),
        None: ('REDUCE', 3),
        'CODE': ('GOTO', 5),
        'VDECL': ('GOTO', 2),
        'FDECL': ('GOTO', 3),
    },
    3: {
        'vtype': ('SHIFT', 4),
        None: ('REDUCE', 3),
        'CODE': ('GOTO', 6),
        'VDECL': ('GOTO', 2),
        'FDECL': ('GOTO', 3),
    },
    4: {
        'id': ('SHIFT', 7),
        'ASSIGN': ('GOTO', 8),
    },
    5: {
        None: ('REDUCE', 1),
    },
    6: {
        None: ('REDUCE', 2),
    },
    7: {
        'semi': ('SHIFT', 9),
        'assign': ('SHIFT', 11),
        'lparen': ('SHIFT', 10),
    },
    8: {
        'semi': ('SHIFT', 12),
    },
    9: {
        'vtype': ('REDUCE', 4),
        'id': ('REDUCE', 4),
        'rbrace': ('REDUCE', 4),
        'if': ('REDUCE', 4),
        'while': ('REDUCE', 4),
        'for': ('REDUCE', 4),
        'return': ('REDUCE', 4),
        None: ('REDUCE', 4),
    },
    10: {
        'vtype': ('SHIFT', 14),
        'rparen': ('REDUCE', 9),
        'ARG': ('GOTO', 13),
    },
    11: {
        'id': ('SHIFT', 21),
        'lparen': ('SHIFT', 20),
        'literal': ('SHIFT', 17),
        'num': ('SHIFT', 22),
        'float': ('SHIFT', 23),
        'RHS': ('GOTO', 15),
        'EXPR': ('GOTO', 16),
        'TERM': ('GOTO', 18),
        'FACTOR': ('GOTO', 19),
    },
    12: {
        'vtype': ('REDUCE', 5),
        'id': ('REDUCE', 5),
        'rbrace': ('REDUCE', 5),
        'if': ('REDUCE', 5),
        'while': ('REDUCE', 5),
        'for': ('REDUCE', 5),
        'return': ('REDUCE', 5),
        None: ('REDUCE', 5),
    },
    13: {
        'rparen': ('SHIFT', 24),
    },
    14: {
        'id': ('SHIFT', 25),
    },
    15: {
        'semi': ('REDUCE', 6),
        'rparen': ('REDUCE', 6),
    },
    16: {
        'semi': ('REDUCE', 21),
        'rparen': ('REDUCE', 21),
    },
    17: {
        'semi': ('REDUCE', 22),
        'rparen': ('REDUCE', 22),
    },
    18: {
        'semi': ('REDUCE', 24),
        'rparen': ('REDUCE', 24),
        'addsub': ('SHIFT', 26),
    },
    19: {
        'semi': ('REDUCE', 26),
        'rparen': ('REDUCE', 26),
        'addsub': ('REDUCE', 26),
        'multdiv': ('SHIFT', 27),
    },
    20: {
        'id': ('SHIFT', 21),
        'lparen': ('SHIFT', 20),
        'num': ('SHIFT', 22),
        'float': ('SHIFT', 23),
        'EXPR': ('GOTO', 28),
        'TERM': ('GOTO', 18),
        'FACTOR': ('GOTO', 19),
    },
    21: {
        'semi': ('REDUCE', 28),
        'rparen': ('REDUCE', 28),
        'addsub': ('REDUCE', 28),
        'multdiv': ('REDUCE', 28),
        'comp': ('REDUCE', 28),
    },
    22: {
        'semi': ('REDUCE', 29),
        'rparen': ('REDUCE', 29),
        'addsub': ('REDUCE', 29),
        'multdiv': ('REDUCE', 29),
        'comp': ('REDUCE', 29),
    },
    23: {
        'semi': ('REDUCE', 30),
        'rparen': ('REDUCE', 30),
        'addsub': ('REDUCE', 30),
        'multdiv': ('REDUCE', 30),
        'comp': ('REDUCE', 30),
    },
    24: {
        'lbrace': ('SHIFT', 29),
    },
    25: {
        'rparen': ('REDUCE', 11),
        'comma': ('SHIFT', 31),
        'MOREARGS': ('GOTO', 30),
    },
    26: {
        'id': ('SHIFT', 21),
        'lparen': ('SHIFT', 20),
        'num': ('SHIFT', 22),
        'float': ('SHIFT', 23),
        'EXPR': ('GOTO', 32),
        'TERM': ('GOTO', 18),
        'FACTOR': ('GOTO', 19),
    },
    27: {
        'id': ('SHIFT', 21),
        'lparen': ('SHIFT', 20),
        'num': ('SHIFT', 22),
        'float': ('SHIFT', 23),
        'TERM': ('GOTO', 33),
        'FACTOR': ('GOTO', 19),
    },
    28: {
        'rparen': ('SHIFT', 34),
    },
    29: {
        'vtype': ('SHIFT', 42),
        'id': ('SHIFT', 43),
        'rbrace': ('REDUCE', 13),
        'if': ('SHIFT', 39),
        'while': ('SHIFT', 40),
        'for': ('SHIFT', 41),
        'return': ('REDUCE', 13),
        'VDECL': ('GOTO', 37),
        'ASSIGN': ('GOTO', 38),
        'BLOCK': ('GOTO', 35),
        'STMT': ('GOTO', 36),
    },
    30: {
        'rparen': ('REDUCE', 8),
    },
    31: {
        'vtype': ('SHIFT', 44),
    },
    32: {
        'semi': ('REDUCE', 23),
        'rparen': ('REDUCE', 23),
    },
    33: {
        'semi': ('REDUCE', 25),
        'rparen': ('REDUCE', 25),
        'addsub': ('REDUCE', 25),
    },
    34: {
        'semi': ('REDUCE', 27),
        'rparen': ('REDUCE', 27),
        'addsub': ('REDUCE', 27),
        'multdiv': ('REDUCE', 27),
        'comp': ('REDUCE', 27),
    },
    35: {
        'return': ('SHIFT', 46),
        'RETURN': ('GOTO', 45),
    },
    36: {
        'vtype': ('SHIFT', 42),
        'id': ('SHIFT', 43),
        'rbrace': ('REDUCE', 13),
        'if': ('SHIFT', 39),
        'while': ('SHIFT', 40),
        'for': ('SHIFT', 41),
        'return': ('REDUCE', 13),
        'VDECL': ('GOTO', 37),
        'ASSIGN': ('GOTO', 38),
        'BLOCK': ('GOTO', 47),
        'STMT': ('GOTO', 36),
    },
    37: {
        'vtype': ('REDUCE', 14),
        'id': ('REDUCE', 14),
        'rbrace': ('REDUCE', 14),
        'if': ('REDUCE', 14),
        'while': ('REDUCE', 14),
        'for': ('REDUCE', 14),
        'return': ('REDUCE', 14),
    },
    38: {
        'semi': ('SHIFT', 48),
    },
    39: {
        'lparen': ('SHIFT', 49),
    },
    40: {
        'lparen': ('SHIFT', 50),
    },
    41: {
        'lparen': ('SHIFT', 51),
    },
    42: {
        'id': ('SHIFT', 52),
        'ASSIGN': ('GOTO', 8),
    },
    43: {
        'assign': ('SHIFT', 11),
    },
    44: {
        'id': ('SHIFT', 53),
    },
    45: {
        'rbrace': ('SHIFT', 54),
    },
    46: {
        'id': ('SHIFT', 21),
        'lparen': ('SHIFT', 20),
        'num': ('SHIFT', 22),
        'float': ('SHIFT', 23),
        'FACTOR': ('GOTO', 55),
    },
    47: {
        'rbrace': ('REDUCE', 12),
        'return': ('REDUCE', 12),
    },
    48: {
        'vtype': ('REDUCE', 15),
        'id': ('REDUCE', 15),
        'rbrace': ('REDUCE', 15),
        'if': ('REDUCE', 15),
        'while': ('REDUCE', 15),
        'for': ('REDUCE', 15),
        'return': ('REDUCE', 15),
    },
    49: {
        'id': ('SHIFT', 21),
        'lparen': ('SHIFT', 20),
        'num': ('SHIFT', 22),
        'float': ('SHIFT', 23),
        'FACTOR': ('GOTO', 57),
        'COND': ('GOTO', 56),
    },
    50: {
        'id': ('SHIFT', 21),
        'lparen': ('SHIFT', 20),
        'num': ('SHIFT', 22),
        'float': ('SHIFT', 23),
        'FACTOR': ('GOTO', 57),
        'COND': ('GOTO', 58),
    },
    51: {
        'id': ('SHIFT', 43),
        'ASSIGN': ('GOTO', 59),
    },
    52: {
        'semi': ('SHIFT', 9),
        'assign': ('SHIFT', 11),
    },
    53: {
        'rparen': ('REDUCE', 11),
        'comma': ('SHIFT', 31),
        'MOREARGS': ('GOTO', 60),
    },
    54: {
        'vtype': ('REDUCE', 7),
        None: ('REDUCE', 7),
    },
    55: {
        'semi': ('SHIFT', 61),
    },
    56: {
        'rparen': ('SHIFT', 62),
    },
    57: {
        'comp': ('SHIFT', 63),
    },
    58: {
        'rparen': ('SHIFT', 64),
    },
    59: {
        'semi': ('SHIFT', 65),
    },
    60: {
        'rparen': ('REDUCE', 10),
    },
    61: {
        'rbrace': ('REDUCE', 32),
    },
    62: {
        'lbrace': ('SHIFT', 66),
    },
    63: {
        'id': ('SHIFT', 21),
        'lparen': ('SHIFT', 20),
        'num': ('SHIFT', 22),
        'float': ('SHIFT', 23),
        'FACTOR': ('GOTO', 67),
    },
    64: {
        'lbrace': ('SHIFT', 68),
    },
    65: {
        'id': ('SHIFT', 21),
        'lparen': ('SHIFT', 20),
        'num': ('SHIFT', 22),
        'float': ('SHIFT', 23),
        'FACTOR': ('GOTO', 57),
        'COND': ('GOTO', 69),
    },
    66: {
        'vtype': ('SHIFT', 42),
        'id': ('SHIFT', 43),
        'rbrace': ('REDUCE', 13),
        'if': ('SHIFT', 39),
        'while': ('SHIFT', 40),
        'for': ('SHIFT', 41),
        'return': ('REDUCE', 13),
        'VDECL': ('GOTO', 37),
        'ASSIGN': ('GOTO', 38),
        'BLOCK': ('GOTO', 70),
        'STMT': ('GOTO', 36),
    },
    67: {
        'semi': ('REDUCE', 31),
        'rparen': ('REDUCE', 31),
    },
    68: {
        'vtype': ('SHIFT', 42),
        'id': ('SHIFT', 43),
        'rbrace': ('REDUCE', 13),
        'if': ('SHIFT', 39),
        'while': ('SHIFT', 40),
        'for': ('SHIFT', 41),
        'return': ('REDUCE', 13),
        'VDECL': ('GOTO', 37),
        'ASSIGN': ('GOTO', 38),
        'BLOCK': ('GOTO', 71),
        'STMT': ('GOTO', 36),
    },
    69: {
        'semi': ('SHIFT', 72),
    },
    70: {
        'rbrace': ('SHIFT', 73),
    },
    71: {
        'rbrace': ('SHIFT', 74),
    },
    72: {
        'id': ('SHIFT', 43),
        'ASSIGN': ('GOTO', 75),
    },
    73: {
        'vtype': ('REDUCE', 20),
        'id': ('REDUCE', 20),
        'rbrace': ('REDUCE', 20),
        'if': ('REDUCE', 20),
        'while': ('REDUCE', 20),
        'for': ('REDUCE', 20),
        'else': ('SHIFT', 77),
        'return': ('REDUCE', 20),
        'ELSE': ('GOTO', 76),
    },
    74: {
        'vtype': ('REDUCE', 17),
        'id': ('REDUCE', 17),
        'rbrace': ('REDUCE', 17),
        'if': ('REDUCE', 17),
        'while': ('REDUCE', 17),
        'for': ('REDUCE', 17),
        'return': ('REDUCE', 17),
    },
    75: {
        'rparen': ('SHIFT', 78),
    },
    76: {
        'vtype': ('REDUCE', 16),
        'id': ('REDUCE', 16),
        'rbrace': ('REDUCE', 16),
        'if': ('REDUCE', 16),
        'while': ('REDUCE', 16),
        'for': ('REDUCE', 16),
        'return': ('REDUCE', 16),
    },
    77: {
        'lbrace': ('SHIFT', 79),
    },
    78: {
        'lbrace': ('SHIFT', 80),
    },
    79: {
        'vtype': ('SHIFT', 42),
        'id': ('SHIFT', 43),
        'rbrace': ('REDUCE', 13),
        'if': ('SHIFT', 39),
        'while': ('SHIFT', 40),
        'for': ('SHIFT', 41),
        'return': ('REDUCE', 13),
        'VDECL': ('GOTO', 37),
        'ASSIGN': ('GOTO', 38),
        'BLOCK': ('GOTO', 81),
        'STMT': ('GOTO', 36),
    },
    80: {
        'vtype': ('SHIFT', 42),
        'id': ('SHIFT', 43),
        'rbrace': ('REDUCE', 13),
        'if': ('SHIFT', 39),
        'while': ('SHIFT', 40),
        'for': ('SHIFT', 41),
        'return': ('REDUCE', 13),
        'VDECL': ('GOTO', 37),
        'ASSIGN': ('GOTO', 38),
        'BLOCK': ('GOTO', 82),
        'STMT': ('GOTO', 36),
    },
    81: {
        'rbrace': ('SHIFT', 83),
    },
    82: {
        'rbrace': ('SHIFT', 84),
    },
    83: {
        'vtype': ('REDUCE', 19),
        'id': ('REDUCE', 19),
        'rbrace': ('REDUCE', 19),
        'if': ('REDUCE', 19),
        'while': ('REDUCE', 19),
        'for': ('REDUCE', 19),
        'return': ('REDUCE', 19),
    },
    84: {
        'vtype': ('REDUCE', 18),
        'id': ('REDUCE', 18),
        'rbrace': ('REDUCE', 18),
        'if': ('REDUCE', 18),
        'while': ('REDUCE', 18),
        'for': ('REDUCE', 18),
        'return': ('REDUCE', 18),
    },
}
