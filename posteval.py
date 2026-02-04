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


def posteval(str):
    num = Stack_t()
    opt = []
    tokenlist=str.split()
    for token in tokenlist:
        if token.isdecimal():
            num.push(token)
        elif  token == "+":
            b = int(num.pop())
            a = int(num.pop())
            num.push(a+b)
        elif  token == "-":
            b = int(num.pop())
            a = int(num.pop())
            num.push(a-b)
        elif  token == "*":
            b = int(num.pop())
            a = int(num.pop())
            num.push(a*b)
        elif  token == "/":
            b = int(num.pop())
            a = int(num.pop())
            num.push(a/b)

    return  num.pop()

str=input()
print(posteval(str))
