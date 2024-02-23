if __name__=='__main__':
        s1 = input('Enter string1: ')
        s2 = input('Enter string2: ')
        ls = len(s1)
        l2 = len(s2)

        def lcs(s1, s2, l1, l2):
            dp = [0] * (l1 + 1)
    
            for i in range(l2):
                temp = [0]
                prev = 0
                for j in range(l1):
                    cur = dp[j + 1]
                    if s1[j] == s2[i]:
                        temp.append(1 + prev)
                    else:
                        temp.append(max(temp[-1], cur))
                    prev = cur
                dp = temp
                # print(dp)
            return dp[-1]
        print(lcs(s1,s2,l1,l2))