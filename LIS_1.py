"""
heres another a version that keeps track of the provess behind

"""

def LIS(arr):
    n = len(arr)
    dp = [1]* n
    prev = [None]*n
    max_len = 1
    max_index = 0
    for i in range(1,n):
        for j in range(i):
            if arr[i] > arr[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j
                if dp[i] > max_len:
                    max_len = dp[i]
                    max_index = i
    lis = []
    while max_index is not None:
        lis.append(arr[max_index])
        max_index = prev[max_index]
    lis.reverse()
    return max_len,lis

arr= input("Enter the array: ")
arr = list(map(int,arr.split()))
max_len,lis = LIS(arr)
print("Length of LIS is:", max_len)
print("The LIS array is:", lis)
