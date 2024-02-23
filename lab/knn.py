import csv, random, math, operator
from collections import Counter

def euclideanDistance(instance1, instance2):
    distance = 0
    for x1,x2 in zip(instance1,instance2):
        distance += pow((x1 - x2), 2)
    return math.sqrt(distance)

def getAccuracy(testSet, predictions):
    correct = 0
    for ex,pred in zip(testSet,predictions):
        if ex[-1] == pred:
            correct += 1
    return (correct/float(len(testSet))) * 100.0

# prepare data
trainingSet=[]
testSet=[]
split = 0.67
for row in csv.reader(open('KNN-input.csv')):
    p = list(map(float,row[:-1]))+[row[-1]]
    if random.random()<split:
        trainingSet.append(p)
    else:
        testSet.append(p)

print ('\n Number of Training data: ' + (repr(len(trainingSet))))
print (' Number of Test Data: ' + (repr(len(testSet))))
# generate predictions
predictions=[]
k = 3
print('\n The predictions are: ')
for x in testSet:
    #get neighbours
    distances = []
    for i in trainingSet:
        dist = euclideanDistance(x[:-1], i[:-1])
        distances.append((i, dist))
    #get k nearest neighbours
    distances.sort(key=operator.itemgetter(1))
    neighbors = [item[0] for item in distances[:k+1]]
    #get response
    d = Counter(z[-1] for z in neighbors)
    result = sorted(d.items(), key = operator.itemgetter(1))[-1][0]
    predictions.append(result)
    print(' predicted=' + repr(result) + ', actual=' + repr(x[-1]))

accuracy = getAccuracy(testSet, predictions)
print('\n The Accuracy is: ' + repr(accuracy) + '%')