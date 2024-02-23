#Kadane' algo : returns maximum sum of a subarray in an array
arr = list(map(int,input('Enter array: ').split()))
summ = 0
max_sum = float('-inf')
for i in arr:
    summ+=i
    if max_sum<summ:
        max_sum = summ
    if summ<0:
        summ = 0

print(f"The max sum of subarray is {max_sum} ")
# Largest sum of subarray of size atleast k
'''
    def maxSumWithK(self, a, n, k):
        # Code here
        ans, prev_sm = float('-inf'), 0
        i = j = sm =  0
        while j<n:
            sm += a[j]
            if j-i+1==k:
                ans = max(ans,sm)
            elif j-i+1>k:
                ans = max(ans,sm)
                prev_sm += a[i]
                i+=1
                if prev_sm<0:
                    sm -= prev_sm
                    ans = max(ans,sm)
                    prev_sm = 0
            j+=1
        return ans
'''