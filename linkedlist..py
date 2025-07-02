class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# --- now, in top‑level code, create and link your nodes ---
node1 = Node('a')
node2 = Node('b')
node3 = Node('c')

node1.next = node2
node2.next = node3

# traverse and print
current_node = node1
while current_node:
    print(current_node.data, end=" -->> ")
    current_node = current_node.next
print("Null")
