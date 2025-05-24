class Solution:
    def checkPerfectSquare (ob,N):
        # code here
        i = 2
        while i < N:
            if N % i == 0 and N == i * i:
                return 1
            i += 1
        return 0