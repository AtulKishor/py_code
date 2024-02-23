import pandas as pd
import math
class Node:
    def __init__(self):
        self.label = 'NULL'
        self.branch = {}

def entropy(data):
    total_ex = len(data)
    p_ex = len(data.loc[data['PlayTennis']=='Yes'])
    n_ex = len(data.loc[data['PlayTennis']=='No'])
    en = 0
    if p_ex>0 :
        en -= (p_ex/float(total_ex)) * (math.log(p_ex,2)-math.log(total_ex,2))
    if n_ex>0 :
        en -= (n_ex/float(total_ex)) * (math.log(n_ex,2)-math.log(total_ex,2))
    return en

def gain(en_s,data_s,attrib):
    gain = en_s
    for value in set(data_s[attrib]):
        gain -= len(data_s.loc[data_s[attrib]==value])/float(len(data_s)) * entropy(data_s.loc[data_s[attrib]==value])
    return gain

def get_attr(data):
    en_s = entropy(data)
    attribute = ""
    max_gain = 0
    for attr in data.columns[:-1]:
        g = gain(en_s, data, attr)
        if g > max_gain:
            max_gain = g
            attribute = attr
    return attribute

def decision_tree(data):
    root = Node()
    if entropy(data)==0:
        if len(data.loc[data[data.columns[-1]]=="Yes"]) == len(data): #number of +ve examples comprises of whole data
            root.label = "Yes"
        else:
            root.label = "No"
        return root
    #base condition: if only labels in data then return 
    # if len(data.columns)==1 :
    #     return
    # else:
    if len(data.columns)>1:
        attr = get_attr(data)
        root.label = attr
        for value in set(data[attr]):
            root.branch[value] = decision_tree(data.loc[data[attr]==value].drop(attr,axis=1))   #data.loc(bool array) returns rows where bool array==True #.drop(attr,axis) => drops col(axis=1) with heading attr
        return root

def get_rules(root, rule, rules):
    if not root.branch: #leaf node
        rules.append(rule[:-1]+"=>"+root.label)
        return
    for val in root.branch:
        get_rules(root.branch[val], rule+root.label+"="+str(val)+"^", rules)
    return rules
    
def test(tree):
    if not tree.branch:
        return tree.label
    return test(tree.branch[str(test_str[tree.label])])

data = pd.read_csv("tennis.csv")
tree = decision_tree(data)
rules = get_rules(tree," ",[])  #rules is an array of string rules
for rule in rules:
    print(rule)
test_str = {} 
print("Enter the test case input: ")
for attr in data.columns[:-1]:#data.columns returns top row([ Outlook,Temperature, Humidity, Windy, PlayTennis])
    test_str[attr] = input(attr+": ")
print(test_str)
print(test(tree))

'''
#tennis.csv
     Outlook Temperature Humidity   Windy PlayTennis
0      Sunny         Hot     High    Weak         No
1      Sunny         Hot     High  Strong         No
2   Overcast         Hot     High    Weak        Yes
3      Rainy        Mild     High    Weak        Yes
4      Rainy        Cool   Normal    Weak        Yes
5      Rainy        Cool   Normal  Strong         No
6   Overcast        Cool   Normal  Strong        Yes
7      Sunny        Mild     High    Weak         No
8      Sunny        Cool   Normal    Weak        Yes
9      Rainy        Mild   Normal    Weak        Yes
10     Sunny        Mild   Normal  Strong        Yes
11  Overcast        Mild     High  Strong        Yes
12  Overcast         Hot   Normal    Weak        Yes
13     Rainy        Mild     High  Strong         No
'''