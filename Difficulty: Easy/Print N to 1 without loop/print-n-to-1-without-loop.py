#User function Template for python3

class Solution:
    def printNos(self, n):
        # Code here
        if 1 > n:
            return 1
        print(n,end = " ")
        return self.printNos(n-1)
        