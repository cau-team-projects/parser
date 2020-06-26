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
    def is_valid(self, state, symbol):
        if self.debug:
            print('Is', state, symbol, 'valid?', state in self.table and symbol in self.table[state])
        return state in self.table and symbol in self.table[state]
    def reduce(self, rule):
        non_terminal, pop_count = self.rules[rule]
        if pop_count > 0:
            self.stack = self.stack[:-pop_count]
        if self.debug:
            print('Reduce to', non_terminal, 'by rule', rule, 'popping', pop_count)
        state = self.state()
        if not self.is_valid(state, non_terminal):
            print('Invalid state or symbol')
            return False
        action, state = self.table[state][non_terminal]
        assert(action == 'GOTO')
        self.goto(state)
        return True
    def goto(self, state):
        if self.debug:
            print('Goto', state)
        self.stack.append(state)
    def state(self):
#        if len(self.stack) < 1:
#            return 0
        return self.stack[-1]
    def decide(self, token):
        terminal, value = token
        while True:
            state = self.state()
            if self.debug:
                print('Stack:', self.stack)
                print('Terminal:', terminal, 'value:', value, 'state:', state)
            if self.is_valid(state, terminal): # non-empty entry of the table
                action, state_rule = self.table[state][terminal]
                # not shifting
            else: # empty entry of the table, something wrong!
                print('Failed to parse at', 'state:', state, 'terminal:', terminal)
                return False, False
            if action == 'SHIFT':
                if self.debug:
                    print('Shift')
                self.goto(state_rule)
                return True, False # shift
            elif action == 'REDUCE':
                ok = self.reduce(state_rule)
                if not ok:
                    print('Reduce failed')
                    return False, False
            elif action == 'ACCEPT':
                return True, True
            else: # neither SHIFT nor REDUCE on terminal
                print('Unknown action')
                return False, False

    def parse(self, infile):
        for token in lexer.lex(infile):
            print('-' * 40)
            ok, accepted = self.decide(token)
            if not ok:
                return False
        ok, accepted = self.decide((None, None)) # terminal = None, value = None
        if not ok:
            return False
        if not accepted:
            print('Not accepted after parse finished')
        return accepted

with open(sys.argv[1], 'r') as infile:
    parser_debug, lexer_debug = False, False
    if 'PARSER_DEBUG' in os.environ:
        parser_debug = (os.environ['PARSER_DEBUG'] == '1')
    if 'LEXER_DEBUG' in os.environ:
        lexer_debug = (os.environ['LEXER_DEBUG'] == '1')

    lexer = Lexer(debug=lexer_debug)

    parser = Parser(lexer, debug=parser_debug)
    print('Accepted:', parser.parse(infile))
