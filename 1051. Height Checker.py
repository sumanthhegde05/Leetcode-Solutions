class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sa = sorted(heights)
        count=0
        for x,y in zip(sa , heights):
            if x!=y:
                count = count+1
        return count
