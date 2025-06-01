class Solution:
    def maxValue(self, arr):
        arr.sort()
        MOD = 10**9 + 7
        return sum((val * i) % MOD for i, val in enumerate(arr)) % MOD