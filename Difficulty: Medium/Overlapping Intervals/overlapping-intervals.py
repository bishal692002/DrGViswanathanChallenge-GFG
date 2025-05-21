class Solution:
    def mergeOverlap(self, arr):
        #Code here
        arr.sort()
        merge=[arr[0]]
        for i in range(len(arr)):
            lmerge=merge[-1]
            if lmerge[1]>=arr[i][0]:
                lmerge[1]=max(lmerge[1],arr[i][1])
            else:
                merge.append(arr[i])
        return merge