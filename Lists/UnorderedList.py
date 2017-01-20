from Node import Node

class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()

        return count

    def search(self, key):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == key:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        previous = None
        current = self.head
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if not found:
            print("Element not found")
            return
        if previous is None and found:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        temp = Node(item)
        temp.setNext(None)

        current = self.head
        while current.getNext() is not None:
            current = current.getNext()

        current.setNext(temp)

    def insert(self, position, item):
        temp = Node(item)
        temp.setNext(None)
        previous = None
        current = self.head
        pos_count = 0

        if position <= 0 or position > self.size()+1:
            print("Invalid position")
            return
        while pos_count != position - 1:
            previous = current
            current = current.getNext()
            pos_count += 1

        if previous is None:
            self.add(item)
        else:
            previous.setNext(temp)
            temp.setNext(current)

    def index(self, item):
        current = self.head
        found = False
        index = 0

        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                index += 1

        return index if found else -1

    def pop(self, pos=-1):
        current = self.head
        previous = None
        if pos != -1:
            if pos > self.size()+1 or pos <= 0:
                # print("Invalid position")
                return
            cur_pos = 0
            while cur_pos != pos-1:
                previous = current
                current = current.getNext()
                cur_pos += 1

            popped_item = current.getData()
            if previous is not None:
                previous.setNext(current.getNext())
            else:
                self.head = current.getNext()
            return popped_item
        else:
            while current.getNext() is not None:
                previous = current
                current = current.getNext()

            previous.setNext(None)
            return current.getData()

    def __str__(self):
        result = "["
        current = self.head

        while current is not None:
            result += str(current.getData())
            current = current.getNext()
            if current:
                result += ", "
        result += "]"
        return result

# mylist = UnorderedList()
#
# mylist.add(31)
# mylist.add(77)
# mylist.add(17)
# mylist.add(93)
# mylist.add(26)
# mylist.add(54)
#
# print(mylist.size())
# print(mylist)
# print(mylist.pop(0))
# print(mylist)
# print(mylist.pop(1))
# print(mylist)
# print(mylist.pop(5))
# print(mylist)
# print(mylist)
# print(mylist.search(100))
#
# mylist.add(100)
# print(mylist.search(100))
# print(mylist.size())
#
# mylist.remove(54)
# print(mylist.size())
# mylist.remove(93)
# print(mylist.size())
# mylist.remove(31)
# print(mylist.size())
# print(mylist.search(93))