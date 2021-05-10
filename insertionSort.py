'''
    Description:  Sorts myList in ascending order using an insertion sort.
    File:  insertionSort.py
'''

import random
import time

def insertionSort(myList):
    """Rearranges the items in myList so they are in ascending order"""
    for firstUnsortedIndex in range(1,len(myList)):
        itemToInsert = myList[firstUnsortedIndex]
        # Scan the sorted part from the right side
        # Shift items to the right while you have not scanned past the left
        # end of the list and you have not found the spot to insert
        testIndex = firstUnsortedIndex - 1
        while testIndex >= 0 and myList[testIndex] > itemToInsert:
            myList[testIndex+1] = myList[testIndex]
            testIndex = testIndex - 1

        # Insert the itemToInsert at the correct spot
        myList[testIndex + 1] = itemToInsert


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
insertionSort(list1)
end = time.time()
print("insertion, Array 1: ", end - start)

fToRead2 = open("array2.txt", "r")
list2 = []
for lineIt in fToRead2:
    list2 = lineIt.split(" ")

start2 = time.time()
insertionSort(list2)
end2 = time.time()
print("insertion, Array 2: ", end2 - start2)
