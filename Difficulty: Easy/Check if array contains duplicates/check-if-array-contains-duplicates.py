
class Solution:

    def checkDuplicates(self, arr):
        #code here
        return len(arr) != len(set(arr))
