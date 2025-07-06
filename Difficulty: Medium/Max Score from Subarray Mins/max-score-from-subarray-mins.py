class Solution:
    def maxSum(self, arr):
        res = 0
        for i in range(len(arr)-1):
                res = max(res, arr[i] + arr[i+1])
        return res