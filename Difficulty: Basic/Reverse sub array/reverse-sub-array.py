#User function Template for python3
class Solution:
	def reverseSubArray(self,arr,l,r):
		while l<=r:
		    arr[l-1],arr[r-1]=arr[r-1],arr[l-1]
		    l+=1
		    r-=1
		return arr