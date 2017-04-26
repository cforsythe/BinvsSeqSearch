import numpy as np
import random
import matplotlib.pyplot as plt
import time

randnum10 = np.random.randint(-10, 11, size = 10); randnum10.sort()
randnum100 = np.random.randint(-100, 101, size = 100); randnum100.sort()
randnum1000 = np.random.randint(-1000, 1001, size = 1000); randnum1000.sort()
randnum10000 = np.random.randint(-10000, 10001, size = 10000); randnum10000.sort()

avgSearchtime = [0,0,0,0]
numarrays = [randnum10,randnum100,randnum1000,randnum10000]
rand10 = {}
rand100 = {}
rand1000 = {}
rand10000 = {}
dictionaries = [rand10, rand100, rand1000, rand10000]

def searchSequential(array, numberToFind):
    operations = 0
    for x in range(0, len(array)):
        operations = operations + 1
        if(array[x] == numberToFind):
            return operations
        else:
            continue
    return operations
def binSearch(array, numberToFind):
    operations = 0
    low = 0; high = len(array) - 1
    while(low <= high):
        operations += 3
        currnum = low + (high - low)/2
        if(array[currnum] == numberToFind):
            return operations
        elif array[currnum] < numberToFind:
            operations += 1
            low = currnum + 1
        else:
            operations += 1
            high = currnum - 1
    return operations

def binSim(sims):
    for array in numarrays:
        for x in range(0, int(sims)):
            startTime = time.time()
            num = binSearch(array, random.randint(-len(array), len(array) + 1))
            avgSearchtime[numarrays.index(array)] += (time.time() - startTime)
            currentdict = dictionaries[numarrays.index(array)]
            currentdict[num] = currentdict.get(num, 0) + 1
def seqSim(sims):
    for array in numarrays:
        for x in range(0, int(sims)):
            startTime = time.time()
            num = searchSequential(array, random.randint(-len(array), len(array) + 1))
            avgSearchtime[numarrays.index(array)] += (time.time() - startTime)
            currentdict = dictionaries[numarrays.index(array)]
            currentdict[num] = currentdict.get(num, 0) + 1

def cleardicts():
    for dict in dictionaries:
        dict.clear()

def graph():
    arraysize = 1
    for numdict in dictionaries:
        arraysize = arraysize * 10
        d = dictionaries[dictionaries.index(numdict)]
        plt.bar(range(len(d)), d.values(), align="center")
        plt.xticks(range(len(d)), list(d.keys()))
        plt.plot()
        plt.title("Array Simulations Array Size " + str(arraysize))
        plt.show()

def main():
    ans = raw_input("How many simulations would you like to run?")
    binSim(ans)
    size = 10
    print("Binary Search")
    for x in range(0, 4):
        print("Array size " + str(size) + str(dictionaries[x]))
        print("Average Time " + str(avgSearchtime[x]/int(ans)) + "\n")
        size *= 10
    graph()
    cleardicts()
    seqSim(ans)
    size = 10
    print("Sequential Search")
    for x in range(0, 4):
        print("Array size " + str(size) + str(dictionaries[x]))
        print("Average Time " + str(avgSearchtime[x]/int(ans)) + "\n")
        size *= 10
    graph()


main()
