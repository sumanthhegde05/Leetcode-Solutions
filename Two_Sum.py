class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        result=[]
        for items in range(0,len(nums)):
            if target-nums[items] not in dictionary:
                dictionary[nums[items]] = items
            else:
                result.append(dictionary[target - nums[items]])
                result.append(items)
        return result
