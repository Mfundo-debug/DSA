"""
Binary search algorithm
function takes an `arr` and a target `x` as input
initializes 3 vars `low`,`high` and `mid` as the first, last and middle elem of the arr respectively
then uses while loop that continues as `low` =< to `high`
within the while loop, calculates the middle idx by taking the avg of `low` and `high`.
rhen it compares the elem at the middle idx with the target elem `x`
if the elem at middle idx < `x`, the `low` idx is set to the middle idx +1, because it means the target elem is in the right half of the arr
if the elem at middlw idx > `x`, the `high` idx is set to the middle idx -1, because it means the target elm is in the left half of the arr.
If the element at the middle index is == to `x`, the function returns the middle index as the position of the target element.
If the target element is not found after the while loop, the function returns -1
"""

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        
        mid = (high + low) // 2
        
        if arr[mid] < x:
            low = mid + 1
            
        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1

arr = input("enter the array: ")
arr = list(map(int,arr.split()))
x = int(input("enter the target element:"))
print(binary_search(arr, x))
