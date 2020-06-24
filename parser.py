import os
import sys
from lexer.lexer import Lexer
import parser.table
import parser.rules

class Parser():
    def __init__(self, lexer, debug=False):
        self.debug = debug
        self.lexer = lexer
        self.table = parser.table.table
        self.rules = parser.rules.rules
        self.START = parser.rules.START
        self.stack = [0]
    def reduce(self, rule):
        non_terminal, pop_count = self.rules[rule]
        if non_terminal == self.START:
            return True # accepted
        self.stack.pop(pop_count)
        action, state = self.table[self.state()][non_terminal]
        assert(action == 'GOTO')
        self.goto(state)
    def goto(self, state):
        self.stack.push(state)
    def state(self):
        return self.stack[-1]
    def parse(self, infile):
        for token in lexer.lex(infile):
            terminal, value = token
            while True:
                state = self.state()
                if state in self.table and terminal in self.table[state]:
                    action, state_rule = self.table[self.state()][terminal]
                else:
                    print('Failed to parse at', 'state:', state, 'terminal:', terminal)
                    return False
                if action == 'SHIFT':
                    self.goto(state_rule)
                    break # shift
                elif action == 'REDUCE':
                    accepted = self.reduce(state_rule)
                    if accepted:
                        return True
                else: # neither SHIFT nor REDUCE on terminal
                    print('Unknown action')
                    return False
        print('Not accepted after parse finished')
        return False

with open(sys.argv[1], 'r') as infile:
    debug = False
    if 'DEBUG' in os.environ:
        debug = (os.environ['DEBUG'] == '1')
    lexer = Lexer(debug=debug)
    parser = Parser(lexer, debug=debug)
    #print(next(parser.parse(infile)))
    #for res in parser.parse(infile):
    #    print('res', res)
    print('Accepted:', parser.parse(infile))

