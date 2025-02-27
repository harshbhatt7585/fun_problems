"""
3. **Two Sum**

Given an array of integers and a target sum, return the indices of the two numbers such that they add up to the target.

**Example:**

Input: [2, 7, 11, 15], target = 9

Output: [0, 1] (because 2 + 7 = 9)
"""

# Time Complexity: O(N)
# Space Complexity: O(N)
def two_sum(array: list, target: int):
    dict_ = {}
    for i, ele in enumerate(array):
        if target - ele in dict_:
            return (dict_[target - ele], i)
        else:
            dict_[ele] = i
    

if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))