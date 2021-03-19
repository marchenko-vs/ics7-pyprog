import random

def selectionSort(array):
    for i in range(len(array) - 1):
        indexMin = i
        for j in range(i+1, len(array)):
            if array[j] < array[indexMin]:
                indexMin = j
        array[indexMin], array[i] = array[i], array[indexMin]
    return array

def bubbleSort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def bubbleSortWithFlag(array):
    for i in range(len(array) - 1):
        flag = True
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = False
        if flag:
            break
    return array

def shakerSort(array):
    left = 0
    right = len(array) - 1
    while left < right:
        rightNew = left
        for i in range(left, right):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                rightNew = i
        right = rightNew
    leftNew = right
    for i in range(right - 1, left - 1, -1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            leftNew = i
        left = leftNew
    return array

def insertionSort(array):
    for i in range(1, len(array)):
        value = array[i]
        j = i - 1
        while (array[j] > value) and (j >= 0):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = value
    return array

def insertionSortWithBarrier(array):
    array = [0] + array
    for i in range(1, len(array)):
        array[0] = array[i]
        j = i - 1
        while array[j] > array[0]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = array[0]
    return array[1:]

def insertionSortWithBinSearch(data):
    for i in range(1, len(data)):
        curr = data[i]
        lo, hi = 0, i
        if lo == hi:
            lo += 1
        else:
            while lo < hi:
                mid = (lo + hi) // 2
                if curr < data[mid]:
                    hi = mid
                else:
                    lo = mid + 1
        j = i
        while j > lo and j > 0:
            data[j] = data[j - 1]
            j -= 1
        data[lo] = curr
    return data

def shellSort(array):
    inc = len(array) // 2
    while inc > 0:
        for i, el in enumerate(array):
            while i >= inc and array[i - inc] > el:
                array[i] = array[i - inc]
                i -= inc
            array[i] = el
        inc = 1 if inc == 2 else int(inc * 5 / 11)
    return array

def quickSort(array, start=0, end=None):
    if len(array) == 0:
        return array
    pind = random.randint(start, end - 1)
    pivot = array[pind]
    left = [x for x in array if x < pivot]
    right = [x for x in array if x > pivot]
    return quickSort(left, 0, len(left)) + [pivot] + quickSort(right, 0, len(right))


lst = [10, -4, -3, -2, -1, 4, 8, 2, 9, 5, 1]
print(shakerSort(lst))
print(shellSort(lst))