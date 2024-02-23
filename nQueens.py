n = int(input('Enter n: '))
state = [['_']*n for _ in range(n)]
res = set()
visited_col = set()
visited_dig = set()
visited_xdig = set()
def backtrack(r):
    if r==n:
        print(*map('|'.join, state),sep='\n')
        res.add(map('#'.join, map(''.join, state))) # add a valid solution
        print()
        return

    for c in range(n):
        if not(c in visited_col or r-c in visited_dig or r+c in visited_xdig):
            visited_col.add(c)
            visited_dig.add(r-c)
            visited_xdig.add(r+c)
            state[r][c]='Q'
            backtrack(r+1)

            visited_col.remove(c)
            visited_dig.remove(r-c)
            visited_xdig.remove(r+c)
            state[r][c]='_'
            


backtrack(0)

input()