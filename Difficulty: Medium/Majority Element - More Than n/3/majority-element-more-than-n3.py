class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        hmap  = {}
        for num in arr:
            if num in hmap:
                hmap[num] += 1
            else:
                hmap[num] = 1
        
        result = []
        for key,value in hmap.items():
            if value>(len(arr)//3):
                result.append(key)
        return sorted(result)


