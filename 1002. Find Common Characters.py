class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        k=list(A[0])
        for i in A:
            nums=[]
            for j in i:
                if j in k:
                    nums.append(j)
                    k.remove(j)
            k=nums
        return nums
                
