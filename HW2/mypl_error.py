#
# Author: Maxwell Sherman
# Course: CPSC 326, Spring 2019
# Assignment: 2
# Description:
#   MyPLError class, to be used in hw2.py
#------------------------------------------

class MyPLError(Exception):
    def __init__(self, message, line, column):
        self.message = message
        self.line = line
        self.column
    
    def __str__(self):
        msg = self.message
        line = self.line
        column = self.column
        return "error: %s at line %i column %i" % (msg, line, column)
