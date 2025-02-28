"""
**Median of Two Sorted Arrays**

Given two sorted arrays of different sizes, find the median of the combined array without fully merging them.

**Example:**

Input: [1, 3], [2]

Output: 2.0

Input: [1, 2], [3, 4]

Output: 2.5
"""


## Does not work, needs to fix
def median_of_array(arr1: list, arr2: list):
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)

    added_len = len_arr1 + len_arr2

    if added_len % 2 != 0:
        if arr1[(len_arr1//2)-1] > arr2[(len_arr2//2)-1]:
            return  arr1[(len_arr1//2)-1]
        else:
            return arr2[(len_arr2//2)-1]
    else:
        done = False
        while not done:
            mid1 = arr1[(len_arr1//2)]
            mid2 = arr2[(len_arr2//2)-1]
            print(mid1)
            print(mid2)
            return ( mid1 + mid2 ) / 2
        


if __name__ == "__main__":
    median = median_of_array([1, 9, 11], [3, 4, 7])
    print(median)
     
    