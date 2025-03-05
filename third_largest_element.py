"""
**Find the third largest element in an array**

**Example**:

Input:

arr = [10, 5, 20, 8, 25, 15]

Output: 15
"""

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n): 
        swapped = False  
        j = 0
        while j < n - i - 1:  
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            
            j += 1
        
        if not swapped: 
            break

    return arr


if __name__ == "__main__":
    arr = [10, 5, 20, 8, 25, 15]
    sorted_arr = bubble_sort(arr)
    third_max = sorted_arr[-3]
    print("Third largest number in the array", third_max)