#User function Template for python3

class Solution:
    def searchInsertK(self, Arr, N, k):
        # code here
        left,right = 0 ,  len(Arr)-1
        
        while left<= right:
            mid = (left + right) // 2

            if Arr[mid] == k:
                return mid
            elif Arr[mid]<k:
                left = mid + 1
            else:
                right = mid-1
        return left
                