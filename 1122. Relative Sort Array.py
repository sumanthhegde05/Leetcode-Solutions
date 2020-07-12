class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        k=[]
        a=[]
        for i in arr2:
            for j in arr1:
                if j==i :
                    k.append(j)
        if len(k)<len(arr1):
            for i in range(0,len(arr1)):
                if arr1[i] not in arr2:
                    a.append(arr1[i])
        a.sort()
        k=k+a
        return k
