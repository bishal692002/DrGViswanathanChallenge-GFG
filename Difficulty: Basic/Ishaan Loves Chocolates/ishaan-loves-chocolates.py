from typing import List


class Solution:
    def chocolates(self, n : int, arr : List[int]) -> int:
        # code here
        minus=arr[0]
        for i in range(n):
            if arr[i]<minus:
                minus=arr[i]
                
        return minus
