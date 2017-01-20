#Node.py
"""
Description :   Definition of Node ADT that will be imported by other programs implementing
                List Data Structure
Author      :   rajath.kiran@gmail.com
"""

class Node:
    def __init__(self,initdata):
        '''
        Initialises the node with initial data
        :param initdata: First data of the node
        '''
        self.data = initdata
        self.next = None

    def getData(self):
        '''
        :return: Returns the data in the node
        '''
        return self.data

    def setData(self,newdata):
        '''
        Sets the node with new data
        :param newdata: Data to be sett
        '''
        self.data = newdata

    def getNext(self):
        '''
        :return: Returns the next node address
        '''
        return self.next

    def setNext(self,newNext):
        '''
        Sets the link of the current node to point to next
        :param newNext: Address of the next node
        :return: None
        '''
        self.next = newNext
