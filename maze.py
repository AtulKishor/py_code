n = int( input('Enter n'))
mat = [list(map(int,input().split())) for i in range(n)]
path_sum = 0
ans = 0
def bt(i,j):
    global path_sum, ans
    #base cond
    if i==n or j==n:
        return

    path_sum += mat[i][j]
    if i==n-1 and j==n-1:
        ans = max(ans,path_sum)

    #bounding function for general case
    if i<n:
        bt(i+1,j)
    if j<n:
        bt(i,j+1)
    

bt(0,0)
print(ans)