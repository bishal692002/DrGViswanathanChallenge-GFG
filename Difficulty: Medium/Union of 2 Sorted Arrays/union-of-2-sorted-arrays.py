class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here 
        s=[]
        seen=set()
        l1=len(a)
        l2=len(b)
        i=0
        j=0
        while i<l1 and j<l2:
            if a[i]<b[j]:
                temp=a[i]
                if temp not in seen:
                    s.append(temp)
                    seen.add(temp)
                i+=1
            else:
                temp=b[j]
                if temp not in seen:
                    s.append(temp)
                    seen.add(temp)
                j+=1
        while i<l1:
            temp=a[i]
            if temp not in seen:
                s.append(temp)
                seen.add(temp)
            i+=1
        while j<l2:
            temp=b[j]
            if temp not in seen:
                s.append(temp)
                seen.add(temp)
            j+=1
            
        return s