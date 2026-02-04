import random

def hash(num):
    key = (num*19)%10
    return key

hashtable = [None] * 10
i=0

while i<9:
    value=random.randint(1, 100)
    key = hash(value)

    while hashtable[key] != None:
        key = (key + 1) % 10
    hashtable[key] = value

    i=i+1

print(hashtable)
    
            
