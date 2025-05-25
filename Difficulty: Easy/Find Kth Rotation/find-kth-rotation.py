class Solution:
    def findKRotation(self, arr):
        n = len(arr)
        min_index = 0
        for i in range(1, n):
            if arr[i] < arr[min_index]:
                min_index = i
        return min_index