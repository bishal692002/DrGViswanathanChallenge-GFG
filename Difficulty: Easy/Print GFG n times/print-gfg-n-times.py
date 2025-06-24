#User function Template for python3

class Solution:
    def printGfg(self, n):

        g="GFG"

        if n==0:

            return ""

        res=self.printGfg(n-1)

        print(g,end=" ")

        return res