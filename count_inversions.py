"""
Count the number of inversions in an unsorted list from a text file.
This is a programming assignment from Coursera's Stanford's Algorithms course.

Specify your file name, expected format is one number per line.
This code is borrowed heavily from my implementation of MergeSort.
The onyl real difference is that we introduce a count variable
"""
FILE_NAME = 'input.txt'

#Read the file into an array
#Expecting one line per number
nums = []

f = open(FILE_NAME)
for line in f:
    nums.append(int(line))
    
#Assignment file in the class should be 100k lines
#assert len(nums) == 100000

#Count the inversions
def sort_count(unsorted_list):
    '''(list) -> sorted list
    
    Will take an unsorted list, run mergesort algorithim and
    return a sorted list.
    '''
    #Make copy of the list
    l = unsorted_list[:] 
    
    #Base Case - List is sorted when length 1 or less
    if len(l) <= 1:
        return l, 0
        
    #Split list
    middle_index = len(l) / 2
    first_half = l[:middle_index]
    second_half = l[middle_index:]
    
    #Recursive Case
    first_half, first_half_count = sort_count(first_half)
    second_half, second_half_count = sort_count(second_half)
    split_list, split_count = merge_count(first_half, second_half)
    
    return split_list, (split_count + first_half_count + second_half_count)
    
def merge_count(first_half, second_half):
    '''(list, list) -> list, int
    
    Will loop through each list at same time, comparing ech element, then
    combining the elements into an output list that is sorted.  Will
    count every time a number is out of order (inversion).
    '''
    count = 0
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
            #Count the inversions as the remaing numbers on the left, not just as 1
            #This is b/c the number is inverted with all the remaining digits as well as the
            #Comparison
            count += len(first_half) - i
    #Append Remainng part of lists
    while i < len(first_half):
        sorted_list.append(first_half[i])
        i += 1
    while j < len(second_half):
        sorted_list.append(second_half[j])
        j += 1
        
    return sorted_list, count
    
#Test case, 3 inversions
a = [1, 3, 5, 2, 4, 6]      
print sort_count(a)

#Test case, 1 inversion
b = [1, 3, 2]
print sort_count(b)

#For the Class - uncomment
#print sort_count(nums)