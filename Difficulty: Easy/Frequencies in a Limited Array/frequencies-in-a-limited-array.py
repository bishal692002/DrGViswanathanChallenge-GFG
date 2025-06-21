class Solution:
    
    def frequencyCount(self, arr):
        freq = {}
        for _ in arr:
            if _ in freq:
                freq[_] += 1
            else:
                freq[_] = 1
        
        result = []
        
        for _ in range(1,len(arr)+1):
            if i in freq:
                result.append(freq[i])
            else:
                result.append(0)
        return result






#{ 
 # Driver Code Starts
# Main code to read input and process each test case
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().frequencyCount(arr)  # find the frequencies

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print the result
    else:
        print("[]")  # Print empty list if no valid frequencies

# } Driver Code Ends