class Solution:
    def countPackets(self, N):
        count = 0
        i = 0
        while N > 0:
            capacity = 2 ** i
            if N >= capacity:
                N -= capacity
            else:
                N = 0
            count += 1
            i += 1
        return count
