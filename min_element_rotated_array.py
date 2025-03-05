"""
**Find the Minimum Element in a Rotated Sorted Array**

Suppose an array sorted in ascending order is rotated at some pivot. Find the minimum element.

**Example:**

Input: [3, 4, 5, 1, 2]

Output: 1
"""




def min_(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid 
    

if  __name__ == "__main__":
    a = [3, 4, 5, 1, 2] 
    min_(a)