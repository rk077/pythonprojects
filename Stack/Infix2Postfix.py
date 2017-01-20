"""
Problem Statement:
Source  :
"""

from Stack import Stack


def infix_to_postfix(input_expr):
    '''
    Converts infix to postfix expression.
    :param input_expr: input expression in infix form
    :return: Output expression in postfix form
    '''
    #We use a dictionary to store the precedence of operators.
    # *,/ and +,- have same precedence, ( has lowest precedence
    precedence = {}
    postfix_expr = []
    precedence['*'] = 3
    precedence['/'] = 3
    precedence['-'] = 2
    precedence['+'] = 2
    precedence['('] = 1

    operator_stack = Stack()

    #Split the stack into tokens
    tokens = input_expr.split()

    for each_token in tokens:
        if each_token in 'QWERTYUIOPASDFGHJKLZXCVBNM9876543210':
            postfix_expr.append(each_token)
        elif each_token == '(':
            operator_stack.push(each_token)
        elif each_token == ')':
            topToken = operator_stack.pop()
            while topToken != '(':
                postfix_expr.append(topToken)
                topToken = operator_stack.pop()
        else:
            while (not operator_stack.isEmpty()) and \
                    (precedence[operator_stack.peek()] >= precedence[each_token]):
                postfix_expr.append(operator_stack.pop())
            operator_stack.push(each_token)

    while not operator_stack.isEmpty():
        postfix_expr.append(operator_stack.pop())
    return "".join(postfix_expr)