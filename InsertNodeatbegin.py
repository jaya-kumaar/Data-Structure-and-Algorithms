class Node:
    def __init__(self,data):
        self.data=data
        self.pointer=None
class linkedList: 
    def __init__(self):
        self.head=None

    def InsertAtBegin(self,data):
        newnode=Node(data)
        if self.head == None:
            self.head = newnode
        else:
            newnode.pointer = self.head
            self.head=newnode

    def display(self):
        current_node=self.head
        while current_node:
            print(current_node.data,end="===>>")
            current_node=current_node.pointer
        print("Null")


obj=linkedList()
obj.InsertAtBegin('10')

obj.InsertAtBegin('20')

obj.InsertAtBegin('30')


obj.display()