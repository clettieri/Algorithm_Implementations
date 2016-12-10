"""
Selection Sort

Selection sort takes an array and sorts it from smallest
to biggest by looping through each value of the array and
finding the smallest value to place at index 0.  It then
loops through a subarray starting at index 1 to find the next
smallest value and place it at index 1, This looping over a 
subarray will continue until all items are sorted.
"""

def swap_values(l, first_index, second_index):
    '''(list, int, int) -> None
    
    Will take the first_index and swap it with the second_index.
    This function modifies the original list.
    '''
    pass

def find_minimum_index(l, start_index):
    '''(list, int) -> int
    
    Will loop through the list starting at start_index
    and return the index of the minimum value.
    '''
    min_value = float('inf')
    min_index = None
    for i in range(start_index, len(l)):
        if l[i] < min_value:
            min_value = l[i]
            min_index = i
    return min_index

def selection_sort(l):
    '''(list) -> list that is sorted
    
    Takes a list, will use selection sort to return
    a sorted list.
    '''
    start_index = 0

test_list = [17, 8, 1, 35, 0, 4, 6, 21, 22, 3, 0]
print selection_sort(test_list)

a = [0, 0, 5, 1, 6, 7]
assert find_minimum_index(a, 2) == 3
assert find_minimum_index(a, 1) == 1