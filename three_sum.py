"""
**3Sum - Find Unique Triplets with Zero Sum**

Given an array of integers, find all unique triplets that sum to zero.

**Example:**

Input: [-1, 0, 1, 2, -1, -4]

Output: [[-1, -1, 2], [-1, 0, 1]]
"""


#  Time Complexity ~ O(N^2)
triplets = set()
array = [-1, 0, 1, 2, -1, -4]
array = sorted(array)

for i in range(len(array)-2):
    point1 = i + 1
    point2 = len(array) - 1
    while point1 < point2:
        total = array[i] + array[point1] + array[point2]
        if  total == 0:
            triplets.add((array[i], array[point2], array[point1]))
            point1 += 1
            point2 -= 1
        elif total < 0:
            point1 += 1
        else:
            point2 -= 1


print(triplets)            