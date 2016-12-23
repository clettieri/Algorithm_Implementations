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
"""


