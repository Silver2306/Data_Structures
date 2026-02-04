class Node(object):

    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None


def add(root, key):

    temp = Node(key)

    if  root is None:
        return temp

    cnode = root
    while cnode is not None:
        if cnode.data > key and cnode.left is not None:
            cnode = cnode.left
        elif cnode.data < key and cnode.right is not None:
            cnode = cnode.right
        else:
            break
    
    if cnode.data > key:
        cnode.left = temp
    elif cnode.data < key:
        cnode.right = temp

    return root

def search(root, key):
    present = False

    while root is not None:
        if root.data == key:
            present = True
            break
        elif key > root.data:
            root = root.right
        else:
            root = root.left

    return present

root = Node(60)
add(root, 10)
add(root, 5)
add(root, 12)

print("Searching for 5: ", search(root, 5))
print("Searching for 12: ", search(root, 12))
print("Searching for 10: ", search(root, 10))
