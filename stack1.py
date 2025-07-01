class stack:
    def __init__(self):
        self.stack=[]

    def push(self,element):
        self.stack.append(element)
        
    def pop(self):
        if self.isEmpty():
            return "the stack is empty"
        return self.stack.pop()
    def peek(self):
        if self.isEmpty():
            return "the stack is empty"
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    def isEmpty(self):
        return len(self.stack)==0
obj=stack()
obj.push('1')
obj.push('3')
obj.push('4')
obj.push('5')
obj.push('6')
print(obj.stack)
print(obj.pop())
print(obj.stack)
print(obj.peek())
print(obj.size())
print(obj.isEmpty())