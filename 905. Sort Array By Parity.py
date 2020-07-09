class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        k=[]
        j=[]
        for i in A:
            if i%2 is 0:
                k.append(i)
            else:
                j.append(i)
        return k+j
