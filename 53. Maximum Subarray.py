import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp=0
        maxx=-sys.maxsize-1
        for item in nums:
            temp=max(item,temp+item)
            if maxx<temp:
                maxx=temp
        return maxx
            
