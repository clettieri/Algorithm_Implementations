"""
Randomized Selection algorithm

Find the i-th smallest element in an array without sorting that array.

To do this we will use the QuickSort partition function.
-First choose a pivot element.
-Partition around that pivot element
-Recursive Base Case if len(array)=1 return
-Recursive Case
---pivot index = i, return pivot value
---pivot index > i, Recurse on subarray from left
---pivot index < i, Recurse on subarray from right

On average this runs in O(n) time, with the best results when the pivot
is the median.
"""
import random

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

def random_select(ls, start, end, order_i):
    '''(list, int, int, int)-> int
    
    Will return the value of the order_i smallest element in array ls.
    '''
    #Base Case
    if len(ls) == 1:
        return ls[0]
        
    #Choose Pivot Index
    pivot_index = random.randint(start, end)
    j = partition(ls, start, end, pivot_index)
    
    #Recursive Cases
    if j == order_i:
        #Return smallest i-th value
        return ls[j-1]
    elif j > order_i:
        #Call left/smaller part of array
        return random_select(ls, start, j-1, order_i)
    elif j < order_i:
        #Call right/ bigger part of array
        return random_select(ls, j+1, end, order_i)
        
   
a = [1,2,3,4,5,6]
assert random_select(a, 0, len(a)-1, 3) == 3

b = [5,1,8,3,2,9,0,4,7,6]
assert random_select(b, 0, len(b)-1, 1) ==  0

print "Success"

