
# coding: utf-8

# In[ ]:


import random
import math

def selection_sort(collection):
    comparisons = 0;
    length = len(collection)
    for i in range(length):
        least = i
        for k in range(i + 1, length):
            comparisons += 1
            if collection[k] < collection[least]:
                least = k
        collection[least], collection[i] = (
            collection[i], collection[least]
        )
    return  comparisons, collection

# In[ ]:


def insertion_sort(array, gap):
    comparisons = 0
    for i in range(gap, len(array)):
        comparisons += 1
        val = array[i]
        j = i
        while j >= gap and array[j - gap] > val:
            array[j] = array[j - gap]
            j -= gap
            comparisons +=1
        array[j] = val

    return comparisons


# In[ ]:


def bubble_sort(data):
    count = 0
    while True:
        swapped = False
        for i in range(1, len(data)):
            count += 1
            if data[i-1] > data[i]:
                data[i-1], data[i] = data[i], data[i-1]
                swapped = True
        if not swapped:
            break
    return count, data


# In[ ]:





# In[ ]:

def get_Unsortedness(data):
    counter = 0;
    comparisons = 0
    for index in range(1, len(data)):
        counter+=1
        while 0 < index and data[index] < data[index - 1]:
            counter += 1
            index -= 1

    return counter


# In[ ]:


def shell_sort_shell(array):
    comparisons = []
    unsortedness = []
    gaps = []

    gap = len(array) // 2
    commulative_comp = 0;

    gaps.append(0)

    ## SHELL SORT IMPLEMENTATION (SHELL'S GAP)
    # loop over the gaps
    while gap > 0:
        gaps.append(gap)
        unsortedness.append(get_Unsortedness(array))
        comparisons.append(commulative_comp)
        #print(commulative_comp, get_Unsortedness(array))
        commulative_comp += insertion_sort(array, gap)
        gap //= 2
    
    comparisons.append(commulative_comp)
    unsortedness.append(0)

    return gaps,comparisons,unsortedness,commulative_comp


# In[ ]:


def shell_sort_ciura(array):
    comparisons = []
    unsortedness = []
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    commulative_comp = 0

    ## SHELL SORT IMPLEMENTATION (CIURA'S GAP)
    # loop over the gaps
    for gap in gaps:
        unsortedness.append(get_Unsortedness(array))
        comparisons.append(commulative_comp)
        commulative_comp += insertion_sort(array, gap)

    comparisons.append(commulative_comp)
    unsortedness.append(0)

    return gaps,comparisons,unsortedness


# In[ ]:

def radix_sort_insert(array, radix=10):
    access = []
    if len(array) == 0:
        return array
    
    minValue = min(array)
    maxValue = max(array)

    # Perform counting sort on each exponent/digit, starting at the least
    # significant digit
    exponent = 1
    while (maxValue - minValue) / exponent >= 1:
        #array = countingSortByDigit(array, radix, exponent, minValue)
        res = radix_insertion_sort(array, 1, exponent, radix)
        access += res[1]
        # print(array)
        exponent *= radix

    return array,access

def radix_insertion_sort(array, gap, exp, radix):
    arr = []
    comparisons = 0
    for i in range(gap, len(array)):
        ctr = 0;
        comparisons += 1
        val = array[i]
        # print (val)
        j = i
        while j >= gap and array[j - gap] / exp % radix > val  / exp % radix:
            ctr += 1
            arr.append((array[j],ctr))
            array[j] = array[j - gap]
            j -= gap
            comparisons +=1
        array[j] = val
        arr.append((array[j],ctr))

    return comparisons, arr

def counting_sort(arr, exp):
    access = []
    n = len(arr)
 
    # The output array elements that will have sorted arr
    output = [0] * (n)
 
    # initialize count array as 0
    count = [0] * (10)
 
    # Store count of occurrences in count[]
    ctr = 0
    for i in range(0, n):
        index = (arr[i]/exp)
        ctr += 1
        # access.append((arr[i], ctr))
        count[ int(math.floor((index)%10)) ] += 1
        ctr = 0
 
    # Change count[i] so that count[i] now contains actual
    #  position of this digit in output array
    for i in range(1,10):
        # print("YYYY")
        count[i] += count[i-1]
 
    # Build the output array
    ctr = 0
    i = n-1
    while i>=0:
        index = (arr[i]/exp)
        ctr += 1
        access.append((arr[i], ctr))
        # print(index)
        output[ count[ int(math.floor((index)%10)) ] - 1] = arr[i]
        count[ int(math.floor((index)%10)) ] -= 1
        i -= 1
        ctr = 0
 
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0,len(arr)):
        arr[i] = output[i]

    return access

def radix_sort_count(arr):
    access = []
    # Find the maximum number to know number of digits
    max1 = max(arr)
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1/exp > 0:
        access += counting_sort(arr,exp)
        # tmp
        #insertion_sort(arr, 1)
        exp *= 10
        # print(arr)

    return access;

DEFAULT_BUCKET_SIZE = 1000
def bucketSort(myList, bucketSize=DEFAULT_BUCKET_SIZE):
    comparisons = 0
    if(len(myList) == 0):
        print('You don\'t have any elements in array!')

    minValue = myList[0]
    maxValue = myList[0]

    # For finding minimum and maximum values
    for i in range(0, len(myList)):
        if myList[i] < minValue:
            minValue = myList[i]
        elif myList[i] > maxValue:
            maxValue = myList[i]

    # Initialize buckets
    bucketCount = int(math.floor((maxValue - minValue) / bucketSize) + 1)
    buckets = []
    for i in range(0, bucketCount):
        buckets.append([])

    # For putting values in buckets
    for i in range(0, len(myList)):
        buckets[int(math.floor((myList[i] - minValue) / bucketSize))].append(myList[i])
        

    # Sort buckets and place back into input array
    sortedArray = []
    for i in range(0, len(buckets)):
        comparisons += insertion_sort(buckets[i],1)
        for j in range(0, len(buckets[i])):
            sortedArray.append(buckets[i][j])


    print("Number of buckets %s", len(buckets))
    for i in range(0, len(buckets)):
         if buckets[i]:
                 print("Buckets ", len(buckets[i]), "First: ", buckets[i][0])
        
    print("Total no. of Comparisons: ", comparisons)
    return sortedArray, buckets, comparisons


def merge(arr, l, m, r):
    # print("HEEEEE")
    swaps = 0
    n1 = m - l + 1
    n2 = r- m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0 , n1):
        L[i] = arr[l + i]
 
    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2 :
        swaps += 1
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

    return swaps

    # print(swaps_)
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
def merge_sort(arr,l,r):
    swaps = 0
    if l < r:

        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = int(math.floor((l+(r-1))/2))
 
        # Sort first and second halves
        swaps += merge_sort(arr, l, m)
        swaps += merge_sort(arr, m+1, r)
        swaps += merge(arr, l, m, r)

        # s = swaps_
        # swaps_ = 0
    return swaps

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
# swaps = 0
def partition(arr,low,high):
    swaps = 0
    counter = 0;
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low , high):
 
        # If current element is smaller than or
        # equal to pivot
        # counter += 1
        if   arr[j] <= pivot:
         
            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
            swaps += 1
            counter += 1
 
    arr[i+1],arr[high] = arr[high],arr[i+1]

    # print (counter)
    return ( i+1 ), swaps
 
# The main function that implements quick_sort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
def quick_sort(arr,low,high):
    swaps = 0
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        result =  partition(arr,low,high)
        pi = result[0]
        swaps += result[1]
        # swaps += result[1]
 
        # Separately sort elements before
        # partition and after partition
        swaps += quick_sort(arr, low, pi-1)
        swaps += quick_sort(arr, pi+1, high)
    return swaps

