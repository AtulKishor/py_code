from DSU import DSU
# G = sorted([....[weight,u,v]...]) #greedy algo
G = [[1, 1, 4], [2, 1, 2], [3, 2, 3], [3, 2, 4], [4, 1, 5], [5, 3, 4], [7, 2, 6], [8, 3, 6], [9, 4, 5]]
def solve(V,edges):
    # edges.sort()
    ans = 0
    dsu = DSU(V)
    for wt,u,v in edges:
        if dsu.find(u)!=dsu.find(v):
            ans += wt
            dsu.union(u,v)
    return ans

print(f'Cost of MST = {solve(6,G)}')