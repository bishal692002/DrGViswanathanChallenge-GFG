from typing import List

class Solution:
    def isFrequencyUnique(self, n: int, arr: List[int]) -> bool:
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        return len(freq.values()) == len(set(freq.values()))
