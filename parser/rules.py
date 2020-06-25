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
    8: ('ARG', 0), 

    # MOREARGS -> comma vtype id MOREARGS
    9: ('MOREARGS', 4) 
    # MOREARGS -> epsilon
    10: ('MOREARGS', 0) 

    # BLOCK -> STMT BLOCK
    11: ('BLOCK', 2)
    # BLOCK -> epsilon
    12: ('BLOCK', 0)

    # STMT -> VDECL
    13: ('STMT', 1)
    # STMT -> ASSIGN semi
    14: ('STMT', 2)
    # STMT -> if lparen COND rparen lbrace BLOCK rbrace ELSE
    15: ('STMT', 8)
    # STMT -> while lparen COND rparen lbrace BLOCK rbrace
    16: ('STMT', 7)
    # STMT -> for lparen ASSIGN semi COND semi ASSIGN rparen lbrace BLOCK rbrace
    17: ('STMT', 11)

    # ELSE -> else lbrace BLOCK rbrace
    18: ('ELSE', 4)
    # ELSE -> epsilon
    19: ('ELSE', 0)

    # RHS -> EXPR
    20: ('RHS', 1)
    # RHS -> literal
    21: ('RHS', 1)
    # EXPR -> TERM addsub EXPR
    22: ('EXPR', 3)
    # EXPR -> TERM
    23: ('EXPR', 1)
    # TERM -> FACTOR multdiv TERM
    24: ('TERM', 3)
    # TERM -> FACTOR
    25: ('TERM', 1)
    # FACTOR -> lparen EXPR rparen
    26: ('FACTOR', 3)
    # FACTOR -> id
    27: ('FACTOR', 1)
    # FACTOR -> num
    28: ('FACTOR', 1)
    # FACTOR -> float
    29: ('FACTOR', 1)
    # COND -> FACTOR comp FACTOR
    30: ('COND', 3)
    # RETURN -> return FACTOR semi
    31: ('RETURN', 3)
}
