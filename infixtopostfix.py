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

def inttopost(str):
    op=Stack_t()
    Postfix=[]
    prec={}
    prec["+"]=3
    prec["-"]=3
    prec["*"]=2
    prec["/"]=2
    prec["^"]=1
    prec["("]=1
    tokenlist=str.split()
    for token in tokenlist:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890" or token.isdecimal():
            Postfix.append(token)
        elif token=="(":
            op.push(token)
        elif  token==")":
            while (not op.is_empty()) and op.top()!="(" :
                Postfix.append(op.pop())
            op.pop()
        else:
            while (not op.is_empty()) and (op.top()!="(")  and (prec[token]>=prec[op.top()]) :
                    Postfix.append(op.pop())
            op.push(token)
        
    while not op.is_empty():
        Postfix.append(op.top())
        op.pop()

    return("  ".join(Postfix))
            
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
peq=inttopost(str)
print("Postfix Equation: ",  peq)
pev=posteval(peq)
print("Postfix Evaluation: ", pev)
