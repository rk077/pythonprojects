"""
Problem Statement: Implementing a simple parenthesis Checker to check if balanced or not
Source  : Programming exercise from Problem Solving with Algorithms and Data Structure
"""

from Stack import Stack

def parenthesisChecker(symbolString):
    """
    Function to parse each symbol present in the string and perform Stack
    operations.
    :param symbolString: Input String
    :return: boolean
    """

    s = Stack()
    index = 0
    balanced = True
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


def matches(open, close):
    """
    Function to check if the closing bracket correctly matches the same kind of
    opening bracket.
    :param open: Opening bracket pushed onto the stack
    :param close: Closing bracket encountered from the string
    :return: boolean
    """
    opens = "({["
    closers = ")}]"
    return opens.index(open) == closers.index(close)

input_str = input("Enter the combination:")
result = parenthesisChecker(input_str)

print(result)
