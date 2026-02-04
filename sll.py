class Node(object):

    def __init__(self, data, next):
        self.data = data
        self.next=next

class SingleList(object):
    head = None
    tail = None

    def show(self):
        print("Linked List: ")
        c_node = self.head
        while c_node is not None:
            print(c_node.data, end="-->" )
            c_node = c_node.next
        print(None)

    def add(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head=self.tail=node
        else:
            self.tail.next = node
            self.tail = node

    def removelast(self):
        node0 = self.head
        while node0.next is not None:
            node1 = node0.next
            if node1.next is None:
                node0.next = None
                self.tail = node0
            else:
                node0 = node0.next

    def removefirst(self):
        node0=self.head
        node1=self.head.next
        self.head = node1
        node0.next=None
        

s = SingleList()
s.add(5)
s.add(10)
s.add(15)
s.show()
s.removelast()
s.show()
s.removefirst()
s.show()

