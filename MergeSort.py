"""
MergeSort

Given an array, mergesort will recursively divide that array
until a subarray is length 0 or 1.  In this base case (length 0 or 1),
the subarray is said to be sorted.  Once the array is split up to the base case,
the merge function is called on each pairing of subarrays.  The merge
function looks at the leading element of each subarray and compares the values,
putting the smaller value into the resulting array first.  The resulting array
is then returned as the function returns back up the recurisve chain.

"""

