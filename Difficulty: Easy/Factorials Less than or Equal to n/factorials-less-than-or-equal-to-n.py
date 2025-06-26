# User function Template for python3

class Solution:
    def factorialNumbers(self, n):
        # code here
        result = []
        current = 1
        i = 1
        while True:
            if i == 1: 
                current = 1
            else:
                current *= i
            
            if current <= n:
                result.append(current)
            else:
                break
            i += 1
        return result