import os
import sys
from lexer.lexer import Lexer
with open(sys.argv[1], 'r') as infile:
    debug = False
    if 'DEBUG' in os.environ:
        debug = (os.environ['DEBUG'] == '1')
    lexer = Lexer(debug=debug)
    for token in lexer.lex(infile):
        print(token)
