# User function Template for python3
class Solution:
    # Function to find maximum product subarray
    def maxProduct(self, arr):
        maxmul = arr[0]

        for i in range(len(arr)):
            cmul = 1
            for j in range(i, len(arr)):
                cmul *= arr[j]
                maxmul = max(cmul, maxmul)

        return maxmul


		                  # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

        print("~")

# } Driver Code Ends