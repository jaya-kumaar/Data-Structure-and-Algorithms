class Node:

    def __init__(self,data):

        self.data=data
        self.pointer=None

class Linkedlist:
    def __init__(self):
        self.head = None

    def AtendInsert(self,data):
        newnode=Node(data)
        
        if self.head is None:
            self.head = newnode  # First node becomes head
            return
        last=self.head

        while last.pointer :
            last=last.pointer
        last.pointer=newnode

    def display(self):
        curr_node=self.head
        while curr_node:
            print(curr_node.data,end="-->")
            curr_node=curr_node.pointer
        print("Null")

obj=Linkedlist()
obj.AtendInsert('q')
obj.AtendInsert('2')

obj.display()
