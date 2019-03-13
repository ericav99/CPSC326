# Author: Maxwell Sherman
# Course: CPSC 326, Spring 2019
# Assignment: 7
# Description:
#   MyPLError class, to be used in hw7.py
#------------------------------------------

class MyPLError(Exception):
    # init method
    def __init__(self, message, line, column):
        self.message = message
        self.line = line
        self.column = column
    
    # str method
    def __str__(self):
        msg = self.message
        line = self.line
        column = self.column
        return "error: %s at line %i column %i" % (msg, line, column)
