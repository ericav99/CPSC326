#!/bin/bash

echo "Test 01"
./hw6.py Testing/hw6_t01.mypl > Testing/hw6_r01.txt 2>&1
echo "Test 02"
./hw6.py Testing/hw6_t02.mypl > Testing/hw6_r02.txt 2>&1
echo "Test 03"
./hw6.py Testing/hw6_t03.mypl > Testing/hw6_r03.txt 2>&1 << END
hello
123
END
echo "Test 04"
./hw6.py Testing/hw6_t04.mypl > Testing/hw6_r04.txt 2>&1
