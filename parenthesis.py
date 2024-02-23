n = int(input('Enter n: '))
ans= []
def backtrack(parenthesis :str, opening :int, closing :int):
	#base case
    if opening==closing==0:
        ans.append(parenthesis)
	#general cases with sentinels
    if opening!=0:
        backtrack(parenthesis+'(',opening-1,closing)
            
    if closing>opening:
        backtrack(parenthesis+')', opening, closing-1)
            
backtrack('(',n-1,n)	#any balanced parenthesis starts with '('            add n-1 '(' and n ')'
print(ans)