#User function Template for python3

class Solution:
    def find(self, arr, x):
        first = 0
        last = 0
        found = -1  

        for i in range(len(arr)):
            if arr[i] == x:
                if found == -1:
                    first = i
                last = i
                found = 1  

        if found == -1:
            return [-1, -1]
        return [first, last]



#{ 
 # Driver Code Starts
t = int(input())  # Number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # Input array for each test case
    x = int(input())  # Element to search for
    ob = Solution()
    ans = ob.find(arr, x)  # Call the find function in the Solution class
    print(*ans)  # Print the result as space-separated values
    print("~")

# } Driver Code Ends