#!/usr/bin/python3
#
# Author: Maxwell Sherman
# Course: CPSC 326, Spring 2019
# Assignment: 1
# Description:
#   Basic program that takes a file of "commands" of the form:
#     left n;
#     right n;
#     up n;
#     down n;
#   where n is an integer, and computes the resulting Euclidean distance.
#-------------------------------------------------------------------------

import sys
import math

class DistanceCalculator(object):
    """Computes the Euclidean distance from a file of basic moves"""
    UP_KEYWORD = "up"
    DOWN_KEYWORD = "down"
    LEFT_KEYWORD = "left"
    RIGHT_KEYWORD = "right"
    
    def __init__(self, input_stream):
        self.input_stream = input_stream
        self.x = 0
        self.y = 0
        self.__parse()
    
    
    def __peek(self):
        """Returns next character keeping it in the stream"""
        pos = self.input_stream.tell()
        symbol = self.input_stream.read(1)
        self.input_stream.seek(pos)
        return symbol
    
    
    def __read(self, n):
        """Reads n characters from the stream"""
        return self.input_stream.read(n)
    
    
    def __parse_space(self):
        """Reads sequence of whitespace characters"""
        while self.__peek().isspace():
            self.__read(1)
    
    
    def __parse_command(self):
        """Reads and returns a sequence of non whitespace characters"""
        command = ''
        while not self.__peek().isspace():
            command += self.__read(1)
        return command
    
    
    def __parse_num(self):
        """Reads an integer string from the stream"""
        num = ''
        if self.__peek() == "-":
            num += self.__read(1)
        
        while self.__peek().isdigit():
            num += self.__read(1)
        try:
            return int(num)
        except Exception:
            raise Exception("invalid number '%s'" % num)
    
    
    def __update_coords(self, command, num):
        """Updates the x and y values according to a command"""
        if command == self.UP_KEYWORD:
            self.y += num
        elif command == self.DOWN_KEYWORD:
            self.y -= num
        elif command == self.LEFT_KEYWORD:
            self.x -= num
        elif command == self.RIGHT_KEYWORD:
            self.x += num
        else:
            raise Exception("invalid number '%s'" % num)
    
    
    def __parse(self):
        """Reads commands from input stream, updating x and y coordinates"""
        # TODO: implement this method using __parse_space(),
        # __parse_command(), __parse_num(), __read(), and __peek()
        while(self.__peek() != ""): # if peek() returns 0B, it's the end of the file
            command = self.__parse_command() # command
            self.__parse_space() # space between command and number
            num = self.__parse_num() # number
            self.__read(1) # semicolon
            self.__parse_space() # space after semicolon
            self.__update_coords(command, num) # update x and y
    
    
    def distance(self):
        """Returns the final Euclidean distance from moves in input stream"""
        return math.sqrt(self.x**2 + self.y**2)



def main(filename):
    try:
        f = open(filename, 'r')
        d = DistanceCalculator(f)
        print('Euclidean distance: %.2f' % d.distance())
        f.close()
    except FileNotFoundError:
        sys.exit('invalid filename %s' % filename)
    except Exception as e:
        f.close()
        sys.exit(e)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: %s file' % sys.argv[0])
    main(sys.argv[1])
