class Solution:
    def binarysearch(self, arr, k):
        l = 0
        right = len(arr) - 1
        ans = -1  

        while l <= right: 
            mid = (l + right) // 2

            if arr[mid] == k:
                ans = mid 
                right = mid - 1  
            elif arr[mid] < k:
                l = mid + 1  
            else:
                right = mid - 1  

        return ans  





#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.binarysearch(arr, k)
        print(res)
        print("~")

# } Driver Code Ends