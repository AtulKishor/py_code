def astar(start,stop):
    open = set()
    open.add(start)
    close = set()
    g = {start:0}
    parent = {start:start}
    while open:
        n = None
        for v in open:
            if n is None or g[v]+h(v)<g[n]+h(n):
                n = v
        # if n==stop or not graph[n]: pass
        # else:
        if n!=stop:
            for m,w in get_neighbours(n): 
                if m not in close and m not in open:
                    open.add(m)
                    g[m] = g[n]+w
                    parent[m] = n
                else:
                    if g[m]>g[n]+w:
                        g[m] = g[n]+w
                        parent[m] = n
                        if m in close:
                            close.remove(m)
                            open.add(m)
        # if not n:
        #     print('no path')
        #     return
        # if n==stop:
        else:
            path = []
            while parent[n]!=n:
                path.append(n)
                n = parent[n]
            path.append(start)
            path.reverse()
            return path
        open.remove(n)
        close.add(n)
    # print('no path')
    # return

graph = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1),('H', 7)] ,
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5), ('J', 3)],
}
def get_neighbours(node):
    return graph[node] if node in graph else None
    
def h(n):
    heur = {'A': 10,
        'B': 8,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0}
    return heur[n]
print(astar('A','J'))
