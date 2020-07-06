class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        for item in nums1:
            result.append(-1)
            start = nums2.index(item)
            for elem in range(start+1,len(nums2)):
                if nums2[elem]>nums2[start]:
                    result[-1]=nums2[elem]
                    break
        return result
                
            
