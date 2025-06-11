#User function Template for python3

class Solution:
    def increment(self, arr, N):
        for i in range(N-1, -1, -1):
            if arr[i] !=  9:
                arr[i] += 1
                return arr
            arr[i] = 0
        arr.insert(0, 1)
        return arr
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        ptr = ob.increment(arr,N)
        for i in ptr:
            print(i,end=" ")
        print()
        print("~")
# } Driver Code Ends