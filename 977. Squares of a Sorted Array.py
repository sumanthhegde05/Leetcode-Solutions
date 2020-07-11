class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        first = 0
        second = index = len(A)-1
        result=[None]*len(A)
        while first<=second:
            if (A[first]**2)>(A[second]**2):
                result[index]=A[first]**2
                first+=1
            else:
                result[index]=A[second]**2
                second-=1
            index-=1
        return result
