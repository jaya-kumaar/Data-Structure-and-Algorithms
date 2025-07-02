class Node:
    def __init__(self,data):
        self.data=data
        self.pointer=None

node1=Node('a')
node2=Node('B')
node3=Node('c')

node1.pointer=node2
node2.pointer=node3
node3.pointer=None

current_node=node1
while current_node:
    print(current_node.data,end="--->>")
    current_node=current_node.pointer
print("Null")