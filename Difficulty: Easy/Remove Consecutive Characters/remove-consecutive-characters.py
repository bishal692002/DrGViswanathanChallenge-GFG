#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, s):
        # code here
        hello = ''
        first = s[0]
        hello += first
        
        
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                hello = hello + s[i]
                
        return hello
            
            