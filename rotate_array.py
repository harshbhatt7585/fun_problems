"""
1. **Rotate Array to the Right by k Steps**

Given an array of integers and a number k, rotate the array to the right by k  steps.

**Example:**

Input: [1, 2, 3, 4, 5, 6, 7],  k = 3

Output: [5, 6, 7, 1, 2, 3, 4]
"""



def rorate_array(array: list, k: int):
    for idx in range(len(array)):
        pop_ele = array.pop(0)
        array.append(pop_ele)
        if idx == k:
            break
        print("Hello")
    return array

## How I am solving it
"""
I am iteratinng to the length of the array, and poping(removing) 
the first element from the list and rotating it by adding to the last
until I reached to the index == k
"""


            
if __name__ == "__main__":
    list_ = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotated_array = rorate_array(list_, k)
    print(rotated_array)

        