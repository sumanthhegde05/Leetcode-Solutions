class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxx=i=0
        j=len(height)-1
        while i<j:
            if height[i]<height[j]:
                area = height[i]*(j-i)
                i+=1
            else:
                area=height[j]*(j-i)
                j-=1
            if area>maxx:
                maxx=area
        return maxx
                
