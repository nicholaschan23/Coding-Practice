# Pathrise Software Engineering

# Find the kth largest element in an unsorted array. 
# Note that it is the kth largest element in the sorted order, 
# not the kth distinct element. 

# What is a second way you might do the same problem? 
# Which approach would you prefer and why?

# sort the array, access the kth element
# k=1, returns largest element
def find_largest1(self, arr: list, k: int) -> int:
    temp = arr.sort()
    return temp[-k]
    # O(NlogN)

def find_largest2(self, arr: list, k: int) -> int:
    temp = arr
    for i in range(0, k-1):
        temp.remove(max(temp))
    return max(temp)
    # O(N) + O(N) = O(N)

# The first approach is preferred due to a better time complexity
