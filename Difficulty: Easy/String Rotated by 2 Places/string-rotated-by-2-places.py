class Solution:
    def isRotated(self, s1, s2):
        if len(s1) != len(s2):
            return False
        if len(s1) < 2:
            return s1 == s2
        
        left= s1[2:] + s1[:2] 
        right = s1[-2:] + s1[:-2]
        
        return s2 == left or s2 == right

