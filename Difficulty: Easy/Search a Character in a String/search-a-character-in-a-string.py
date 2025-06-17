#User function Template for python3
class Solution:
    
    # Function to search for a character in the string
    def searchCharacter(self, s, ch):
        # code here
        for i in range(len(s)):
            if ch in s:
                return s.index(ch)
            else:
                return -1