"""
Problem Statement:
Source  :
"""
from Stack import Stack

def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

    remStack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remStack.push(rem)
        decNumber //= base

    convertednum = ""
    while not remStack.isEmpty():
        convertednum += digits[remStack.pop()]

    print(convertednum)

decNum = int(input("Enter decimal number to convert: "))
base = int(input("Enter base: "))
baseConverter(decNum, base)
