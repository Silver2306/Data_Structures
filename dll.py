class Node(object):

    def  __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleList(object):
    head = None
    tail = None

    def show(self):
        print("Linked List: ")
        c_node = self.tail
        while c_node is not None:
            print(c_node.data, end="-->" )
            c_node = c_node.prev
        print(None)

    def add(self, data):
        node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def remove(self):
        node0 = self.tail
        node1 = node0.prev
        self.tail = node1
        node1.next = self.tail

D = DoubleList()
D.add(5)
D.add(10)
D.add(15)
D.show()
D.remove()
D.show()
            
