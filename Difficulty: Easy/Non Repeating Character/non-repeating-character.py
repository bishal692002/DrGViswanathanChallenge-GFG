class Solution:
    def nonRepeatingChar(self,s):
        #code here
        hmap = {}
        for char in s:
            hmap[char] = hmap.get(char, 0) + 1

        
        for char in s:
            if hmap[char] == 1:
                return char
        
        return -1 