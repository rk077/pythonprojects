"""
Problem Statement:
Source  :
"""

from Stack import Stack


def decimal2binary(decimalno):
    s = Stack()

    while decimalno > 0:
        rem = decimalno % 2
        s.push(rem)
        decimalno //= 2

    binaryNo = ""
    while not s.isEmpty():
        binaryNo += str(s.pop())

    print(binaryNo)

inputNo = int(input("Enter decimal number:\n"))
decimal2binary(inputNo)

