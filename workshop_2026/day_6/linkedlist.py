class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
Node1=Node(10)
Node2=Node(20)
Node1.next=Node2
print(Node1.data)

# insert at beginning
noden=Node(5)
noden.next=Node1

# traversal
temp = noden
while temp :
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")

# insert in end
node3=Node(30)
temp=noden
while temp.next:
    temp = temp.next
temp.next=node3
        
# insert in between
node4 = Node(15)

temp = noden

while temp.data != 10:
    temp = temp.next

node4.next = temp.next
temp.next = node4
# traversal again
temp = noden
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")



