class Solution:
    
    def getSingle(self, arr):
        hmap = {}
        for num in arr:
            hmap[num] = hmap.get(num, 0) + 1
            
        for num in hmap:
            if hmap[num] % 2 != 0:
                return num