class Solution:
    def setMatrixZeroes(self, mat):
        # code here
        arr=[]
        brr=[]
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    arr.append(i)
                    brr.append(j)
        arr=list(set(arr))
        brr=list(set(brr))
        for i in range(n):
            for j in range(m):
                if i in arr or j in brr:
                    mat[i][j]=0
        return mat
        # code here
        