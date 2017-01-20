#Stack.py
"""
Description :   Definition of Stack ADT that will be imported by other programs implementing
                Stack Data Structure
Assumption  :   End of the list will hold the top most element of the stack
Author      :   rajath.kiran@gmail.com
Date        :   23-11-2016
"""
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        for eachItem in self.items:
            print(eachItem, sep=',')
