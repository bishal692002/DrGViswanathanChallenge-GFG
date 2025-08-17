class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        f = -1
        s = -1
        for num in arr:
            if num > f:
                s = f
                f = num
            elif s < num <f:
                s = num
        return s