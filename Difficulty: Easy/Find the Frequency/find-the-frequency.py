"""
You're given an array (arr)
Return the frequency of element x in the given array
"""
class Solution:
    def findFrequency(self, arr, x):
        # code here
        count = 0
        for i  in range(len(arr)):
            if arr[i] == x:
                count += 1
        return count