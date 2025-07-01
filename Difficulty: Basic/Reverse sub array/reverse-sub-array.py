class Solution:
	def reverseSubArray(self,arr,L,R):
        L -= 1
        R -= 1
        arr[L:R+1] = reversed(arr[L:R+1])
        
        return arr