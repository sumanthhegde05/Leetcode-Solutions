class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        z = nums1+nums2
        z.sort()
        size = len(nums1)+len(nums2)
        if size%2==0:
            return (z[int(size/2)]+z[int(size/2)-1])/2
        else:
            return z[int(size/2)]
            
