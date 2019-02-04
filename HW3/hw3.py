#!/usr/bin/python3
#
# Author: Maxwell Sherman
# Course: CPSC 326, Spring 2019
# Assignment: 3
# Description:
#   Syntax checker for MyPL
#------------------------------------------

import mypl_error as error
import mypl_token as token
import mypl_lexer as lexer
import mypl_parser as parser
import sys

# main driver function
def main(filename):
    try:
        file_stream = open(filename, "r")
        the_lexer = lexer.Lexer(file_stream)
        the_parser = parser.Parser(the_lexer)
        hw3(the_parser)
        file_stream.close()
    except FileNotFoundError:
        sys.exit("invalid filename %s" % filename)
    except error.MyPLError as e:
        file_stream.close()
        sys.exit(e)

# main helper function
# analyzes tokens from lexer to make sure they fit the MyPL grammar
def hw3(the_parser):
    the_parser.parse()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: %s file" % sys.argv[0])
    main(sys.argv[1])
