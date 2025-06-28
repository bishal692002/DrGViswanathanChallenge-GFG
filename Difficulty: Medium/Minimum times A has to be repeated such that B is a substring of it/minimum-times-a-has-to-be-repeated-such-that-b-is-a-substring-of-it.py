class Solution:
   def minRepeats(self, A, B):
       # code here 
       n = len(B) // len(A)
       
       if B in A * n: 
           return n
       if B in A * (n + 1): 
           return n + 1
       if B in A * (n + 2): 
           return n + 2
       
       return -1