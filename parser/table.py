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
        'ARG': ('GOTO', 13)
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

    }
}
