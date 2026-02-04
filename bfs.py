from queue import Queue

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bitvector = {  'A':0,
                         'B':0,
                         'C':0,
                         'D':0,
                         'E':0,
                         'F':0}

q = Queue();
op=[]
first = 'A'
q.put(first)
bitvector[first]=1

while not q.empty():
    n0 = q.get()
    op.append(n0)
    for i in graph[n0]:
        if bitvector[i]==0:
            q.put(i)
            bitvector[i]=1

print("Breadth First Search: ")
print(op)
