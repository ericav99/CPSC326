#!/usr/bin/python3
#
# Author: Maxwell Sherman
# Course: CPSC 326, Spring 2019
# Assignment: 10
# Description:
#   Higher order function examples in Python
#--------------------------------------------

l = [i for i in range(10)]

def myMap(func, lst):
    return [func(item) for item in lst]

print(myMap(lambda x: x % 2 == 0, l)) # check if even
print(myMap(lambda x: x % 2 == 0, [])) # empty list
print(myMap(lambda x: x + 1, l)) # add 1
