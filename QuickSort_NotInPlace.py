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
-Combine subarrays

NOTE - this implementation is not considered to be "in place."  This is a very
simple implementation to fundamentally understand how QuickSort works.  However,
since it requires creating new subararys, therefore using more memory, this 
impementation is not "in place."
"""

import random

#Create random list
data = random.sample(range(10), 10)
print "Original List:"
print data

def quicksort(ls):
    '''(list) -> sorted list
    
    Will run quicksort algorithm to sort a given list.
    '''
    #Check Recursive Base Case
    if len(ls) < 2:
        return ls
    
    #Choose Pivot Element (this implementation chooses right most element)
    pivot_index = len(ls) - 1
    
    #Partition the array - sort into left/right arrays
    left = [] #less than pivot element
    right = [] #greater than pivot element
    middle = [] #equal to pivot element
    for element in ls:
        if element > ls[pivot_index]:
            right.append(element)
        elif element < ls[pivot_index]:
            left.append(element)
        else:
            middle.append(element)
            
    #Recursively Call on sublists while Combining the end result
    return quicksort(left) + middle + quicksort(right)
    
print "QuickSort List:"
print quicksort(data)
    
    
a = [2, 8, 9, 1, 0, 3, 7, 6, 4, 5]
assert quicksort(a) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

b = [1]
assert quicksort(b) == [1]

c = [0, 2, 1, 2, 4, 3, 5]
assert quicksort(c) == [0, 1, 2, 2, 3, 4, 5]
        
    
