import itertools

n = int(input('Enter n: '))
print('enter matrix of order {N}x{N}'.format(N=str(n)))

mat = [list(map(int,input().split())) for i in range(n)]


cost = 0
seq = ['R']*(n-1)+['B']*(n-1)
for path in list(itertools.permutations(seq)):
 i=0;j=0
 cur = mat[0][0]
 for val in path:
  if val=='R':
   j+=1
   cur+=mat[i][j]

  if val=='B':
   i+=1
   cur+=mat[i][j]

 cost=max(cost,cur)
 
print(cost)