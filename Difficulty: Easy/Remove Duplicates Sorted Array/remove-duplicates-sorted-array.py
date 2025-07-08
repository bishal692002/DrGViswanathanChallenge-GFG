class Solution:
    def removeDuplicates(self, arr):
        if not arr:
            return 0

        index = 1  
        for i in range(1, len(arr)):
            if arr[i] != arr[i - 1]:
                arr[index] = arr[i]
                index += 1

        return index