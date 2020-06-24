import lexer.table
import lexer.tokens

class Lexer:
    def __init__(self, debug=False):
        self.debug = debug
        self.state = 0
        self.tokenval = []
        self.table = lexer.table.table
        self.tokens = lexer.tokens.tokens
    def mktoken(self):
        return (self.tokens[self.state], ''.join(self.tokenval[:-1]))
    def prtoken(self):
        print('<%s, %s>' % self.mktoken())
    def lex(self, infile):
        linenum = 0
        for line in infile:
            linenum += 1
            if self.debug:
                print('line', linenum)
            for char in line:
                self.tokenval.append(char)
                while True:
                    if self.debug:
                        print('-' * 10)
                        print('cur state', self.state)
                        print('new char', char)
                    # if able to proceed
                    if char in self.table[self.state]: 
                        if self.table[self.state][char] != -1:
                            self.state = self.table[self.state][char]
                        elif self.debug:
                            print('pass')
                        if self.debug:
                            print('next state', self.state)
                    # if state is final state and unable to proceed
                    elif self.state in self.tokens:
                        if self.debug:
                            self.prtoken()
                        yield self.mktoken()
                        self.state = 0
                        self.tokenval = self.tokenval[-1:]
                        continue
                    # if state is not final state and unable to proceed
                    else: 
                        print('failed to lex at state [%d] at char [%s] at line %d[%s]' % (self.state, char, linenum, line))
                        return
                    break
        # token state
        if self.state in self.tokens:
            if self.debug:
                self.prtoken()
            yield self.mktoken()
            return
        # state 0
        elif self.state == 0:
            if self.debug:
                print('state 0')
        # wrong state
        else:
            print('failed to lex due to wrong state')
            return
