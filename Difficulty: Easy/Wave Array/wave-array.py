from typing import List

class Solution:
    def convertToWave(self, arr: List[int]) -> None:
        for i in range(0, len(arr)  - 1, 2):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]