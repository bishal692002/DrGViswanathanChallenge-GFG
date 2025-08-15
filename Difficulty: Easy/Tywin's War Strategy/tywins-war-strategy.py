import math 
class Solution:
    def minSoldiers(self, arr, k):
        # code here
        
        arr2 = sorted([k-i%k for i in arr if i%k!=0])
        zeros = int(math.ceil(len(arr)/2)) - (len(arr)-len(arr2))
        
        if zeros <= 0 : return 0
        
        return sum(arr2[:zeros])