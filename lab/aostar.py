class Graph:
    def __init__(self, graph, hlist, startNode):
        self.graph = graph
        self.h = hlist
        self.start = startNode
        
        self.parent = {}
        self.status = {}
        self.sol = {}

    def applyAOStar(self):
        self.aoStar(self.start, False)

    def getNeighbours(self, v):
        return self.graph.get(v,'')

    def getStatus(self, v):
        return self.status.get(v, 0)

    def setStatus(self, v, val):
        self.status[v] = val

    def getHnode(self, n):
        return self.h.get(n,0)

    def setHnode(self, n, val):
        self.h[n]=val

    def printSol(self):
        print("for graph sol, traverse from start node: ", self.start)
        print('--------------------------------------')
        print(self.sol)
        print('--------------------------------------')
        
    def minCostChild(self, v):
        minCost = 0
        costdict={minCost:[]}
        flag = True #no minCost has been calculated yet
        for option in self.getNeighbours(v):
            cost = 0
            nodeList = []
            for c, w in option:
                cost += self.getHnode(c)+w
                nodeList.append(c)
            if flag:
                minCost = cost
                costdict[minCost]=nodeList
                flag = False
            elif minCost>cost:#prev option minCost is larger
                minCost = cost
                costdict[minCost]=nodeList
        return minCost, costdict[minCost]

    def aoStar(self, v, bt):
        print(self.h, self.sol, sep = '\n')
        print('process ', v)
        if self.getStatus(v)>=0:
            minCost, child = self.minCostChild(v)
            print(minCost, child)
            self.setHnode(v,minCost)
            self.setStatus(v,len(child))
            solved = True
            for node in child:
                self.parent[node]=v
                if self.getStatus(node)!=-1:
                    solved &= False
            if solved:
                self.setStatus(v,-1)
                self.sol[v] = child
            if v!= self.start:
                print('here')
                self.aoStar(self.parent[v], True)
            if not bt:
                for node in child:
                    self.setStatus(node, 0)
                    #input(f'{self.parent,self.status}')
                    self.aoStar(node, False)

h = {'A':1, 'B':6, 'C':2, 'D':12, 'E':2, 'F':1, 'G':5, 'H':7, 'I':7, 'J':1}
g = {
    'A':  [ [('B',1),('C',1)], [('D',1)] ],
    'B':  [ [('G',1),('H',1)] ],
    'C':  [ [('J',1)] ],
    'D':  [ [('E',1),('F',1)] ],
    'G':  [ [('I',1)] ]
    
}
g1 = Graph(g,h,'A')
g1.applyAOStar()
g1.printSol()
