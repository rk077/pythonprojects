"""
Problem Statement:
Source  :
"""

from Stack import Stack
import sys

def postfix_evaluation(postfix_expr):
    """

    :param postfix_expr:
    :return:
    """

    tokens = postfix_expr.split()

    oper_stack = Stack()

    for eachToken in tokens:
        if eachToken in "9876543210":
            oper_stack.push(int(eachToken))
        else:
            operand1 = oper_stack.pop()
            operand2 = oper_stack.pop()
            result = doMath(operand1, eachToken, operand2)
            oper_stack.push(result)

    return oper_stack.pop()


def doMath(oper1, operator, oper2):
    """

    :param oper1:
    :param operator:
    :param oper2:
    :return:
    """
    if operator == '+':
        return oper1 + oper2
    elif operator == '-':
        return oper1 - oper2
    elif operator == '*':
        return oper1 * oper2
    else:
        return oper1 / oper2

user_input = input("Enter the postfix expression: ")
print(postfix_evaluation(user_input))
