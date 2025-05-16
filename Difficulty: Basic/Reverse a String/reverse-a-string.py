#User function Template for python3

class Solution:
     def reverseString(self, s: str) -> str:
        # code here
        s = list(s)
        left = 0
        right = len(s)-1
        while left<right:
            s[left],s[right] = s[right],s[left]
            left += 1
            right -=1
        return ''.join(s)
        





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while (t > 0):
        s = input()
        ob = Solution()
        print(ob.reverseString(s))
        t = t - 1

        print("~")

# } Driver Code Ends