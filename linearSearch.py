"""
Linear Search algorithm,
user will be prompted to enter the array
then enter the element that wants to be found in an arr
if found it returns the index of the value if not return -1
"""
def lin_search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = input("enter the array: ")
arr = list(map(int,arr.split()))
x = int(input("enter the key value needs to be searched: "))

print(lin_search(arr,x))

