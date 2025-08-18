class Solution:
    def minMaxCandy(self, prices, k):
        # code here
        prices.sort()
        n = len(prices)
        mini = 0
        maxi = 0
        # res = []
        i,j = 0 , n-1
        while(i<=j):
            mini += prices[i]
            i += 1
            j -= k
            
        i,j = 0 , n-1
        while(i<=j):
            maxi += prices[j]
            j -= 1
            i += k
        
        return [mini,maxi]
            