"""
Insertion Sort

Will sort an array by looping through each element in the array one at a time.
The current element at the right is the new unsorted element, it is then compared
to each element to the left until its proper place is found.  On each comparison
if the current element being placed is lower then the elements in the sorted
part of the array are shifted to the right, this repeates until the current element
is greater than a left most element, that is the new location for this value.

Think of Insertion Sort as what you do when you are sorting a hand of playing 
cards in order. You take one card and move it to its correct location, then take 
the next, etc.
"""

def insertion_sort(l):
    '''(list) -> sorted list
    
    Takes a list, will apply insertion sort algorithm and return a sorted
    list.
    '''
    
    #Outer Loop - through each element
    for i in range(len(l)):
        j = i
        #Inner Loop - compare each element to the left, one at a time
        while j > 0 and l[j-1] > l[j]:
            #While still elements to check and the element to left is
            #greater than unsorted element, swap
            l[j-1], l[j] = l[j], l[j-1] #Swap array elements
            j -= 1
    return l
    
a = [3, 1, 2, 0, 4]
print insertion_sort(a)