#User function Template for python3

class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        d={}
        for i in arr:
            d[i]=d.get(i,0)+1
        key=""
        value=0
        for i,j in d.items():
            if j>value or (j==value and i<key):
                value=j
                key=i
        return key,value