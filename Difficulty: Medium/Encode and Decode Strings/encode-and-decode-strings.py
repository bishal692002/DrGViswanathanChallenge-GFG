class Solution:
    def __init__(self):
        self.v = []

    def encode(self, strs):
        self.v = strs
        return ''.join(strs)

    def decode(self, s):
        return self.v
