class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        result=[]
        for item in range(0,len(nums)):
            if target-nums[item] not in dictionary:
                dictionary[nums[item]] = item
            else:
                result.append(dictionary[target - nums[item]])
                result.append(item)
        return result
