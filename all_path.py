#print all paths from 0,0 to m,n in mXn grid using recursion
paths = []
m,n = map(int,input('Enter m,n sep by space: ').split())
def  bt(i,j,cur_path):
    if not 0<=i<m or not 0<=j<n or (i,j) in cur_path:
        return
    if i==m-1 and j==n-1:
        paths.append(cur_path+[(i,j)])
        return
    cur_path.append((i,j))
    #4 direction
    bt(i,j-1,cur_path)
    bt(i,j+1,cur_path)
    bt(i-1,j,cur_path)
    bt(i+1,j,cur_path)
    
    ##8 direction
    # bt(i-1,j-1,cur_path)
    # bt(i-1,j+1,cur_path)
    # bt(i+1,j-1,cur_path)
    # bt(i+1,j+1,cur_path)
    
    cur_path.pop()

bt(0,0,[])
print(*paths,sep='\n')
