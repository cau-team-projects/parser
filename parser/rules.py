START = 'START' # start symbol
rules = {
    #   NONTERM, POPLEN
    0: ('START', 1), # START -> CODE
    1: ('CODE', 2), # CODE -> VDECL CODE
    2: ('CODE', 2), # CODE -> FDECL CODE
    3: ('CODE', 0), # CODE -> epsilon
    4: ('VDECL', 3), # VDECL -> vtype id semi
    5: ('VDECL', 3), # VDECL -> vtype ASSIGN semi
}
