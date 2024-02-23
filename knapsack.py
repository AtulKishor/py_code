print('KnapSack')
n = int(input('Enter no. of items: '))
W = int(input('Enter capacity of bag: '))
print('Enter weight,profit of %d items separate by space on each line: '%n)
items = sorted([tuple(map(int,input().split())) for i in range(n)])
print("Your items: ",items)

dp = [0]*(W+1)
matrix = []# for repr
for w,p in items:
    temp = dp[:w]
    for j in range(w,W+1):
        temp.append(max(dp[j],p+dp[j-w]))
    dp = temp
    matrix.append(dp.copy())#
print(*matrix,sep='\n')#

print("Max profit = ",dp[-1])

print("Bag:")##
