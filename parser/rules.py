START = 'START' # start symbol
rules = {
    #   NONTERM, POPLEN
    # START -> CODE
    0: ('START', 1), 

    # CODE -> VDECL CODE
    1: ('CODE', 2), 
    # CODE -> FDECL CODE
    2: ('CODE', 2), 
    # CODE -> epsilon
    3: ('CODE', 0), 

    # VDECL -> vtype id semi
    4: ('VDECL', 3), 
    # VDECL -> vtype ASSIGN semi
    5: ('VDECL', 3), 

    # ASSIGN -> id assign RHS
    6: ('ASSIGN', 3), 

    # FDECL -> vtype id lparen ARG rparen lbrace BLOCK RETURN rbrace
    7: ('FDECL', 9), 

    # ARG -> vtype id MOREARGS
    8: ('ARG', 3), 
    # ARG -> epsilon
    9: ('ARG', 0), 

    # MOREARGS -> comma vtype id MOREARGS
    10: ('MOREARGS', 4) 
    # MOREARGS -> epsilon
    11: ('MOREARGS', 0) 

    # BLOCK -> STMT BLOCK
    12: ('BLOCK', 2)
    # BLOCK -> epsilon
    13: ('BLOCK', 0)

    # STMT -> VDECL
    14: ('STMT', 1)
    # STMT -> ASSIGN semi
    15: ('STMT', 2)
    # STMT -> if lparen COND rparen lbrace BLOCK rbrace ELSE
    16: ('STMT', 8)
    # STMT -> while lparen COND rparen lbrace BLOCK rbrace
    17: ('STMT', 7)
    # STMT -> for lparen ASSIGN semi COND semi ASSIGN rparen lbrace BLOCK rbrace
    18: ('STMT', 11)

    # ELSE -> else lbrace BLOCK rbrace
    19: ('ELSE', 4)
    # ELSE -> epsilon
    20: ('ELSE', 0)

    # RHS -> EXPR
    21: ('RHS', 1)
    # RHS -> literal
    22: ('RHS', 1)
    # EXPR -> TERM addsub EXPR
    23: ('EXPR', 3)
    # EXPR -> TERM
    24: ('EXPR', 1)
    # TERM -> FACTOR multdiv TERM
    25: ('TERM', 3)
    # TERM -> FACTOR
    26: ('TERM', 1)
    # FACTOR -> lparen EXPR rparen
    27: ('FACTOR', 3)
    # FACTOR -> id
    28: ('FACTOR', 1)
    # FACTOR -> num
    29: ('FACTOR', 1)
    # FACTOR -> float
    30: ('FACTOR', 1)
    # COND -> FACTOR comp FACTOR
    31: ('COND', 3)
    # RETURN -> return FACTOR semi
    32: ('RETURN', 3)
}
