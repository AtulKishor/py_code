def load_graph():
    n = int(input('Enter number of nodes: '))
    adj = [[] for _ in range(n)]
    e = int(input('Enter number of edges: '))
    print("Enter graph \nsource destination weight")
    for i in range(e):
        src,dst,wt = map(int,input().split())
        adj[src].append((dst,wt))
        adj[dst].append((src,wt))
        
    src = int(input("Enter source: "))
    return adj,n,src
    
choice = input("Want to enter graph? y/n: ")
if choice.startswith(('y','Y')) :
    graph,n,src = load_graph()
else:
    graph,n,src = [[(1,1),(2,5)],[(0,1),(2,1)],[(0,5),(1,1)]] , 3, 0
    print("Graph loaded :")
    print('   ',1)
    print('    /\\')
    print('   /  \\')
    print('  1    1')
    print(' /\t\\')
    print('/\t \\')
    print(0,'---5---',2)
    print(f"source is : {src}")

import heapq
inf = float('inf')
heap = [(0,src)]
distances = [inf]*n
distances[src] = 0

while heap:
    dist,node = heapq.heappop(heap)
    for adj,cost in graph[node]:
        if dist + cost < distances[adj]:
            distances[adj] = dist + cost
            heapq.heappush(heap,(distances[adj],adj))

for i in range(n):
    print(f"distance from source {src} to destination {i} is {distances[i]}")
