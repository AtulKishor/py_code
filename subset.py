print('subset sum problem - 0/1 knapsack')
nums = sorted(map(int,input('Enter numbers in set: ').split()))
d = int(input('Enter subset sum: '))
dp = [False]*(d+1)
dp[0] = True

'''
def bb(cur :int, sum: int):
    #bounding function 
    if sum>d and cur<=d:
        pass

bb(0,sum(l))
print(ans)
'''
print("DP Table: ")
print(' ', *range(d+1), sep = '\t')

for num in nums:
    temp = dp.copy()
    for j in range(num, d+1):
        if dp[j-num]: temp[j] = True
    dp = temp
    print(num, *dp, sep = '\t') 

if not dp[-1]:
    print('No subset possible')
