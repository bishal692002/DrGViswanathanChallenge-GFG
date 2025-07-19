class Solution:
    
    # Function to check if a string is Pangram or not.
    def checkPangram(self, s):
        s = s.lower()
        alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
        return alphabet_set.issubset(set(s))
