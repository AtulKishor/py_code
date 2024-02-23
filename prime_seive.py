def get_primes(n):
    p = 3
    sieve = [1 for _ in range(n+1)]
    while p*p <= n:
        if sieve[p]:
            for x in range(p*p, n+1, 2*p):
                sieve[x] = 0
        p += 2
    ret = [2]
    for i in range(3, n+1, 2):
        if sieve[i]:
            ret.append(i)
    return ret
#PRIMES = set(get_primes(10**5)) # set for efficient search
print(get_primes(100))
'''
1111111110 1  1  1  1  1  0  1  1  1  1  1  0  1  1  1  0  1  0  1  1
0123456789 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
'''