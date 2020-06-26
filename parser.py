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
        self.stack = []
    def is_valid(self, state, symbol):
        print('is valid?', state, symbol)
        return state in self.table and symbol in self.table[state]
    def reduce(self, rule):
        state = self.state()
        non_terminal, pop_count = self.rules[rule]
        self.stack = self.stack[:-pop_count]
        print('reduce', rule, 'pop', pop_count)
        if not self.is_valid(state, non_terminal):
            print('wrong state or symbol')
            return False
        action, state = self.table[state][non_terminal]
        assert(action == 'GOTO')
        self.goto(state)
    def goto(self, state):
        print('goto', state)
        self.stack.append(state)
    def state(self):
        if len(self.stack) < 1:
            return 0
        return self.stack[-1]
    def parse(self, infile):
        for token in lexer.lex(infile):
            terminal, value = token
            while True:
                print('stack:', self.stack)
                state = self.state()
                print('terminal:', terminal, 'value:', value, 'state:', state)
                # non-empty entry of the table
                if self.is_valid(state, terminal):
                    action, state_rule = self.table[state][terminal]
                    # not shifting
                # empty entry of the table, something wrong!
                else:
                    print(self.is_valid(state, terminal), 'Failed to parse at', 'state:', state, 'terminal:', terminal)
                    return False
                if action == 'SHIFT':
                    print('shift')
                    self.goto(state_rule)
                    break # shift
                elif action == 'REDUCE':
                    self.reduce(state_rule)
                elif action == 'ACCEPT':
                    return True
                else: # neither SHIFT nor REDUCE on terminal
                    print('Unknown action')
                    return False
        terminal = None
        value = None
        while True:
            print('stack:', self.stack)
            state = self.state()
            print('terminal:', terminal, 'value:', value, 'state:', state)
            if state in self.table and terminal in self.table[state]:
                action, state_rule = self.table[state][terminal]
                # not shifting
            else:
                print('Failed to parse at', 'state:', state, 'terminal:', terminal)
                return False
            if action == 'SHIFT':
                self.goto(state_rule)
                break # shift
            elif action == 'REDUCE':
                self.reduce(state_rule)
            elif action == 'ACCEPT':
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

    #for res in parser.parse(infile):
    #    print('res', res)

    #print(next(parser.parse(infile)))

    #for token in lexer.lex(infile):
    #    print(token)

    parser = Parser(lexer, debug=debug)
    print('Accepted:', parser.parse(infile))
    
