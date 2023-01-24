"""
Dynamic programming algorithm
Longest Increasing Subsequence (LIS)
function takes an arr `arr` as input
initializes an arr dp of length `n` with all elms as 1
note: min len(LIS) is always 1
uses nested loops to iterate over the arr
outer loop starts from the 2nd elm (idx 1) and goes till the end of the arr
the inner loop starts from 1st elm (idx 0) and goes till the current elm of the outer loop
if the elm of the outer loop (for i) is > than the elm of inner loop (for j) and lis (dp) ending withe inner loop elem +1 is > than LIS elm ending with current elm of outer loop, the LIS ending with current element of outer loop is updated
"""

def LIS(arr):
    n = len(arr)
    dp = [1]* n
    for i in range(1,n):
        for j in range(i):
            if arr[i] > arr[j] and dp[j] + 1:
                dp[i] = dp[j] + 1
    return max(dp)

arr= input("Enter the array: ")
arr = list(map(int,arr.split()))
print("Length of LIS is:", LIS(arr))