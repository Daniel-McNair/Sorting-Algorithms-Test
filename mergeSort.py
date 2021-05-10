"""
File: mergeSort.py

Recursive implementation of mergeSort
"""

import random
import time

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1




fToRead = open("array1.txt", "r")
list1 = []
for lineIt in fToRead:
    list1 = lineIt.split(" ")

start = time.time()
mergeSort(list1)
end = time.time()
print("Merge, Array 1: ", end - start)

fToRead2 = open("array2.txt", "r")
list2 = []
for lineIt in fToRead2:
    list2 = lineIt.split(" ")

start2 = time.time()
mergeSort(list2)
end2 = time.time()
print("Merge, Array 2: ", end2 - start2)