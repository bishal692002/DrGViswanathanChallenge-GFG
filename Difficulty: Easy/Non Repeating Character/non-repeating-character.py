class Solution:
    def nonRepeatingChar(self,s):
        #code here
        hmap = {}
        for char in s:
            if char in hmap:
                hmap[char] += 1
            else:
                hmap[char] = 1
        
        for char in s:
            if hmap[char] == 1:
                return char
        
        return '$' 