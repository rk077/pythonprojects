from Stack import Stack

s = Stack()
print("Is the stack empty? ", s.isEmpty())
s.push(4)
s.push('dog')
print("Top of stack - ", s.peek())
s.push(True)
s.push(8.4)
print("Is the stack empty? ", s.isEmpty())

print(s.pop())
print("Top of stack - ", s.peek())
print(s.pop())
print("Top of stack - ", s.peek())
print("Size of stack is %d" % s.size())
