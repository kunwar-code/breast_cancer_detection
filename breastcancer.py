import math
import operator
import csv
import random

def loadDataset(filename, split, trainingSet=[],testSet=[]):
    with  open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset=list(lines)
        for x in range(len(dataset)-1):
            for y in range(30):
                dataset[x][y]= float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])
 
def euclideanDistance(instance1, instance2, length):
    distance=0
    for x in range(length):
        distance+=pow((instance1[x]-instance2[x]),2)
    return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
    distances=[]
    length=30
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance,trainingSet[x],length)
        distances.append((trainingSet[x],dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors=[]
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

def getResponse(neighbors):
    m =0
    b=0
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response=='M':
            m+=1
        else:
            b+=1
    if m>b:
        return 'M'
    else:
        return 'B'

def getAccuracy(testSet, predictions):
    correct=0
    for x in range(len(testSet)):
        if testSet[x][-1] is predictions[x]:
            correct+=1
    return (correct/float(len(testSet)))*100.0

def main():
    trainingSet =[]
    testSet=[]
    loadDataset(r'data.csv',0.66,trainingSet,testSet)
    predictions=[]
    k=23 #dataset length is 569 so the value of k for optimal result is sqrt(564) which round downs to 23
    for x in range(len(testSet)):
        neighbors= getNeighbors(trainingSet, testSet[x], k)
        result= getResponse(neighbors)
        predictions.append(result)
        #print('> predicted = '+ repr(result) + ', actual = ' + repr(testSet[x][-1]))
    accuracy = getAccuracy(testSet, predictions)
    print('Accurracy : '+ repr(accuracy) + '%')
main()
