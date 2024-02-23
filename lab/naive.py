import pandas as pd
data = pd.read_csv('data.csv')
te = len(data)
np = len(data.loc[data[data.columns[-1]]=='Yes'])
nn = te-np
train = data.sample(frac=0.75)
test = pd.concat([data, train]).drop_duplicates(keep=False)
prob = {}

for col in train.columns[:-1]:
    prob[col] = {}
    for val in set(train[col]):
        temp = train.loc[train[col]==val]
        fpp= len(temp.loc[temp[temp.columns[-1]]=="Yes"])
        fpn= len(temp)-fpp
        prob[col][val] = [fpp/np, fpn/nn]

pred = []
corr = 0
p_yes = np/te
p_no = nn/te
for i in range(len(test)):
    row = test.iloc[i]
    a = p_yes
    b = p_no
    for col in test.columns[:-1]:
        a*=prob[col][row[col]][0]
        b*=prob[col][row[col]][1]
    if a>b:
        pred.append("Yes")
    else:
        pred.append("No")
    if pred[-1]==row[-1]:
        corr+=1

print(corr,pred,test[test.columns[-1]],sep='\n')    