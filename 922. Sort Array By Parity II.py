class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        ans = []
        j=0
        k=1
        for i in range (0,len(A)):
            if A[i]%2==0:
                ans.insert(j,A[i])
                j+=2
            else:
                ans.insert(k,A[i])
                k+=2
        return ans
