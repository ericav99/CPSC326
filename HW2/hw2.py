#!/usr/bin/python3
#
# Author: Maxwell Sherman
# Course: CPSC 326, Spring 2019
# Assignment: 2
# Description:
#   Lexical analyzer for MyPL
#------------------------------------------

import mypl_token as token
import mypl_lexer as lexer
import mypl_error as error
import sys

# main driver function
def main(filename):
    try:
        file_stream = open(filename, "r")
        hw2(file_stream)
        file_stream.close()
    except FileNotFoundError:
        sys.exit("invalid filename %s" % filename)
    except error.MyPLError as e:
        file_stream.close()
        sys.exit(e)

# main helper function
# generates tokens until receiving the EOS token
def hw2(file_stream):
    the_lexer = lexer.Lexer(file_stream)
    the_token = the_lexer.next_token()
    while the_token.tokentype != token.EOS:
        print(the_token)
        the_token = the_lexer.next_token()
    print(the_token)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: %s file" % sys.argv[0])
    main(sys.argv[1])
