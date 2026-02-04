class Stack_t:
    def __init__(self):
        self.demostack=[]

    def push(self, a):
        self.demostack.append(a);

    def pop(self):
        if  self.is_empty():
            return -1
        else:
            return self.demostack.pop()

    def top(self):
        n=len(self.demostack)
        if(n==0):
            return -1
        else:
            return self.demostack[n-1]

    def  is_empty(self):
        n=len(self.demostack)
        if(n==0):
            return 1
        else:
            return 0

d = Stack_t()
d.push(1)
d.push(2)
d.push(3)
print(d.demostack)
print(d.pop())
print(d.top())
print(d.is_empty())
print(d.demostack)

            
