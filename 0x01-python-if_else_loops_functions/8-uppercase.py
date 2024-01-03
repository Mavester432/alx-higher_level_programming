#!/usr/bin/python3
def uppercase(input_str):
    for char in input_str:
        print(chr(ord(char) - 32), end='')
    print()
