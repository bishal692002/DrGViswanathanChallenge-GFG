#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        result = []
        for i in range(len(arr)):
            summ = 0
            for j in range(i, len(arr)):
                summ += arr[j]
                if summ == target:
                    return [i + 1, j + 1]  
                elif summ > target:
                    break  

        return [-1]  







#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subarraySum(arr, d)
        print(" ".join(map(str, result)))
        tc -= 1
        print("~")

# } Driver Code Ends