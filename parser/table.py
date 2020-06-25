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
        'FDECL', ('GOTO', 3),
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
    }

}
