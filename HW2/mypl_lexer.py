#
# Author: Maxwell Sherman
# Course: CPSC 326, Spring 2019
# Assignment: 2
# Description:
#   Lexer class, to be used in hw2.py
#------------------------------------------

import mypl_token as token
import mypl_error as error

class Lexer(object):
    def __init__(self, input_stream):
        self.line = 1
        self.column = 0
        self.input_stream = input_stream
    
    def __peek(self):
        pos = self.input_stream.read(1)
        symbol = self.input_stream.read(1)
        self.input_stream.seek(pos)
        return symbol
    
    def __read(self):
        return self.input_stream.read(1)
    
    def next_token(self):
        # TODO
