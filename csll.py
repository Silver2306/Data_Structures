class Node(object):

    def __init__(self, data, next):
        self.data = data
        self.next = next

class CirSingleList(object):
    head = None
    tail = None

    def show(self):
        print("Linked List: ")
        c_node = self.head
        while True:
            print(c_node.data, end="-->" )
            c_node = c_node.next
            if(c_node == self.head):
                print(c_node.data)
                break
            
    def add(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head=self.tail=node
        else:
            self.tail.next = node
            self.tail = node
        self.tail.next = self.head

c = CirSingleList()
c.add(5)
c.add(10)
c.add(15)
c.show()
        
