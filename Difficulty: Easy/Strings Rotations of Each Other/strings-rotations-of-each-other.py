class Solution:
    def areRotations(self,s1,s2):
        if len(s1) != len(s2):
            return False
        s3 = s1 + s1
        # print(s3)
        return s2 in s3