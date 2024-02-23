import pandas as pd
import numpy as np
data = pd.read_csv('Training_examples.csv')
concept = np.array(data)[:,:-1]
print("The concepts to be learned")
print(concept)
target = np.array(data)[:,-1]
print("\nLabels specific to the concepts\n")
print(target)
print("\n")
def learn(concept,target):
    specific_h = concept[0].copy()
    n = len(specific_h)
    general_h = [['?']*n for i in range(n)]
    for i,h in enumerate(concept):
        if target[i]=='Yes':
            for j in range(n):
                if h[j]!=specific_h[j]:
                    specific_h[j]='?'
                    general_h[j][j]='?'
        else:
            for j in range(n):
                if h[j]!=specific_h[j]:
                    general_h[j][j]=specific_h[j]
                else:
                    general_h[j][j]='?'
        print(i,specific_h,general_h)
    '''
    indices = [i for i,val in enumerate(general_h) if val==['?' for i in range(n)]]
    for i in indices:
        general_h.remove(['?' for j in range(n)])'''
    while general_h.count(['?']*n):
        general_h.remove(['?']*n)
    return specific_h,general_h

s_final, g_final = learn(concept,target)
print("Final S: ", s_final)
print("Final G: ", g_final)
