# Disjoint set - find and union (rank and size) - T.C = O(4alpha)===O(1)
class DSU:
    def __init__(self,n) -> None:
        self.rank = [0]*(n+1)
        self.parent = [i for i in range(n+1)]
        # self.size = [1]*(n+1)
    def find(self,node):
        if node==self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node]) # path compression
        return self.parent[node]

    def union(self,u,v):
        pu, pv = map(self.find,[u,v])
        if pu==pv: return # same parent
        # print(pu,pv)

        if self.rank[pu]<self.rank[pv]: #
            self.parent[pu] = pv 
            # self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu 
            if self.rank[pu]==self.rank[pv]: #
                self.rank[pu]+=1 #
            # self.size[pu] += self.size[pv]
print("Hi")