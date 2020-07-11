class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        a=[]
        for i in range (0,len(A)):
            if A[i] not in a:
                 a.append(A[i])
            else:    
                 return A[i]
        return
