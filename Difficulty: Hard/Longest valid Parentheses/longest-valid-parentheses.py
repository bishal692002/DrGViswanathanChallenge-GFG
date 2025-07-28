
class Solution:
    def maxLength(self, s):
        start1,start2,curr1,curr2,n,ans=0,0,0,0,len(s),0
        for i in range(n):
            if s[i]=="(":
                start1+=1
            else:
                if start1:
                    start1-=1
                    curr1+=2
                    if not start1:
                        ans=max(ans,curr1)
                else:
                    curr1=0
            if s[n-1-i]==")":
                start2+=1
            else:
                if start2:
                    start2-=1
                    curr2+=2
                    if not start2:
                        ans=max(ans,curr2)
                else:
                    curr2=0
        return ans