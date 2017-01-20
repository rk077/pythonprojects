"""
Problem Statement:
Source  :
"""

from Stack import Stack


def takeInput():
    """

    :return:
    """
    query_count = int(input())
    output_string = []
    foodstack = Stack()
    index = 0
    for index in range(0, query_count):
        query = input()
        if len(query) == 1:
            if foodstack.isEmpty():
                output_string.append("No Food")
            else:
                output_string.append(foodstack.pop())
        else:
            price = query.split()
            foodstack.push(price[1])
        index += 1
    index = 0
    print(*output_string,sep='\n')

    #print(strdp[::-1])



takeInput()