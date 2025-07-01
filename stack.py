list = []

list.append('hi')
list.append('hello')
list.append('kumar')
list.append(" ")
print(list)

# pop the element in the stack
list.pop()
list.pop()
list.pop()
list.pop()
print("list after pop:", list)

# peek element in the stack

# isEmpty
isempyt = not bool(list)
if isempyt == True:
    print(True)
else:
    peek_element = list[-1]
    print(peek_element)

# size of stack
size = len(list)
print("size of the stack:", size)
