"""
QuickSort

Divide and Conquer Sorting Algorithm
Average runtime is O(n log n)

-Choose any element in initial array as your pivot.
-Re-arrange elements in this array so that all elements with values less than
pivot are to the left of pivot in the array, and all elements who's value is
greater than pivot element is to the right of the pivot in the array
-Recursively sort the left and right sub-arrays (exlude the pivot element)
-Recursive base case is len(subarray) < 2, array of length 1 or 0 is sorted
-Combine subarrays - nothing to return/ combine since the elements are being
swapped around the pivot element in the current array, nothing to be returned.

"""

import random

#Create random list
data = random.sample(range(10), 10)
print "Original List:"
print data

def partition(ls, start, end, pivot_index):
    '''(list, int, int ,int) -> int
    
    Will sort the array in place around the pivot index value.
    Returns the new location of the pivot
    '''
    #Swap the pivot into the start of this subarray
    ls[start], ls[pivot_index] = ls[pivot_index], ls[start]
    pivot_value = ls[start]
    #Counters not including the location of pivot
    i = start + 1 #Keeps index for where left array ends (less than element)
    j = start + 1 #Moves through the array to end to check each element
    #Loop through subarray
    while j <= end:
        if ls[j] <= pivot_value:
            #If Value is less than pivot Swap it 
            ls[j], ls[i] = ls[i], ls[j]
            i += 1
        j += 1
    #Swap the pivot element back in place
    ls[start], ls[i - 1] = ls[i - 1], ls[start]
    #Return the current index of pivot element
    return i-1

def quicksort(ls, start=0, end=None):
    '''(list, int, int) -> None 
    
    Will run quicksort algorithm to sort a given list. Sorts the list in place.
    '''
    #Set end index if None
    if end is None:
        end = len(ls) - 1
        
    #Check Recursive Base Case
    if end - start < 1:
        return
        
    #Choose Pivot Element
    pivot_index = random.randint(start, end)
    
    #Partition the array - sort the array around the pivot element
    i = partition(ls, start, end, pivot_index)
    
    #Recursively call quicksort() on left and right arrays 
    #The sub arrays unsorted around the pivot
    quicksort(ls, start, i-1)
    quicksort(ls, i+1, end)
    #Don't need to return anything since elements are being swapped in place

    
print "QuickSort List:"
quicksort(data)
print data
    
    
a = [2, 8, 9, 1, 0, 3, 7, 6, 4, 5]
quicksort(a) 
assert a == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

b = [1]
quicksort(b)
assert b == [1]

c = [0, 2, 1, 2, 4, 3, 5]
quicksort(c) 
assert c == [0, 1, 2, 2, 3, 4, 5]
        
    
