"""
MergeSort

Given an array, mergesort will recursively divide that array
until a subarray is length 0 or 1.  In this base case (length 0 or 1),
the subarray is said to be sorted.  Once the array is split up to the base case,
the merge function is called on each pairing of subarrays.  The merge
function looks at the leading element of each subarray and compares the values,
putting the smaller value into the resulting array first.  The resulting array
is then returned as the function returns back up the recurisve chain.

Pseudocode:

merge_sort(list)
-base case if lenght of list <= 1 return list
-split list
-call merge_sort(list_first_half), merge_sort(list_second_half)
-return merge(first, second lists)

merge(first, second)
-sorted_list = []
-compare each elemnt of both lists, append smaller to sorted list
and increment the list taken from, if either list empty, append rest of other list
-return sorted_list
"""

def merge_sort(unsorted_list):
    '''(list) -> sorted list
    
    Will take an unsorted list, run mergesort algorithim and
    return a sorted list.
    '''
    #Make copy of the list
    l = unsorted_list[:] 
    
    #Base Case - List is sorted when length 1 or less
    if len(l) <= 1:
        return l
        
    #Split list
    middle_index = len(l) / 2
    first_half = l[:middle_index]
    second_half = l[middle_index:]

    #Recursively Call merge_sort
    first_half = merge_sort(first_half)
    second_half = merge_sort(second_half)
    
    return merge(first_half, second_half)
    
def merge(first_half, second_half):
    '''(list, list) -> sorted list
    
    Will loop through each list at same time, comparing ech element, then
    combining the elements into an output list that is sorted.
    '''
    sorted_list = []
    i = 0
    j = 0
    #Compare each element from both halves of the list
    while i < len(first_half) and j < len(second_half):
        #Append the smaller element first
        if first_half[i] < second_half[j]:
            sorted_list.append(first_half[i])
            i += 1
        elif second_half[j] < first_half[i]:
            sorted_list.append(second_half[j])
            j += 1  
    #Append Remainng part of lists
    while i < len(first_half):
        sorted_list.append(first_half[i])
        i += 1
    while j < len(second_half):
        sorted_list.append(second_half[j])
        j += 1
        
    return sorted_list
            

    
a = [3,7,1,4,5,8,0,9,2,0]
print merge_sort(a)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    