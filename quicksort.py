"""
quicksort algorithm is a divde- and - conquer that works by partitioning
an array into smaller-sub arrays, one containing elements less than a pivot element
and other containing greater than a pivot element
"""
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

a = input("enter values you want sort: ")
a = list(map(int,a.split()))
print(quicksort(a))
         