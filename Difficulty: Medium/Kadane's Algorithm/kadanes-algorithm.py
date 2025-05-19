class Solution:
    def maxSubArraySum(self, arr):
        # Your code here
        current = 0
        maxi = float('-inf')
        for i in range(len(arr)):
            current += arr[i]
            maxi = max(current,maxi)
            if current < 0:
                current = 0
        return maxi
        
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends