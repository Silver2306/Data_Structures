class Node(object):

    def  __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev

class CirDoubleList(object):
    head = None
    tail = None

    def show(self):
        print("Linked List: ")
        c_node = self.tail
        while True:
            print(c_node.data, end="-->" )
            c_node = c_node.prev
            if(c_node == self.tail):
                print(c_node.data)
                break
        

    def add(self, data):
        node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.tail.next = self.head
        self.head.prev = self.tail
        
D = CirDoubleList()
D.add(5)
D.add(10)
D.add(15)
D.show()
            
