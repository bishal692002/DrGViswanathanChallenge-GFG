#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here
        temp = n
        length = len(str(n)) 
        result = 0
        while(n != 0):
            digit  = n % 10
            result = result + digit ** length
            n = n // 10
        if result == temp:
            return True
        
        return False