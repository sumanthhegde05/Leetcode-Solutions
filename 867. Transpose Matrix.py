class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        k=[[None]*len(A) for i in range(len(A[0]))]
        for i in range (len(A)):
            for j in range (len(A[0])):
                k[j][i]=A[i][j]
        return k
