class Node:
    def __init__(self,data):
        self.data=data
        self.pointer=None
class Linkedlist:
    def __init__(self):
        self.head = None

    def AtBeginInsert(self,data):
        newnode=Node(data)
        if self.head == None:
            self.head = newnode

        else:
            newnode.pointer=self.head
            self.head= newnode

    def AtIndexInsert(self,data,index):

        if index == 0:
            
            AtBeginInser(data)
            return
        
        position =0
        current_node=self.head

        while current_node is not None and position +1 !=index:
            position +=1
            current_node = current_node.pointer

        if current_node is not None:
            newnode = Node(data)
            newnode.pointer =current_node.pointer
            current_node.pointer = newnode
        else:
            print("Index out range")

    def display(self):
            temp=self.head
            while temp:
                print(temp.data,end="-")
                temp =temp.pointer
            print("null")

obj=Linkedlist()
obj.AtBeginInsert('10')
obj.AtBeginInsert('20')
obj.AtBeginInsert('30')
obj.AtBeginInsert('40')


obj.AtIndexInsert('50',2)
obj.display()