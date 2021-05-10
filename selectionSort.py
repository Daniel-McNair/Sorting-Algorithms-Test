'''
    Description:  Sorts myList in ascending order using an selection sort.
    File:  selectionSort.py
'''

import random
import time

def selectionSort(aList):
    for lastUnsortedIndex in range(len(aList)-1, 0, -1):
        # look for maximum item in unsorted part of list
        # Assume maximum is the first item in the unsorted part
        maxIndex = 0

        # scan the unsorted part of the list to correct the assumption
        for testIndex in range(1, lastUnsortedIndex+1):
            if aList[testIndex] > aList[maxIndex]:
                maxIndex = testIndex

        # exchange the items at maxIndex and firstUnsortedIndex
        temp = aList[lastUnsortedIndex]
        aList[lastUnsortedIndex] = aList[maxIndex]
        aList[maxIndex] = temp
        

def shuffle(myList):
    for fromIndex in range(len(myList)):
        toIndex = random.randint(0,len(myList)-1)
        temp = myList[fromIndex]
        myList[fromIndex] = myList[toIndex]
        myList[toIndex] = temp
    



fToRead = open("array1.txt", "r")
list1 = []
for lineIt in fToRead:
    list1 = lineIt.split(" ")

start = time.time()
selectionSort(list1)
end = time.time()
print("selection, Array 1: ", end - start)

fToRead2 = open("array2.txt", "r")
list2 = []
for lineIt in fToRead2:
    list2 = lineIt.split(" ")

start2 = time.time()
selectionSort(list2)
end2 = time.time()
print("selection, Array 2: ", end2 - start2)