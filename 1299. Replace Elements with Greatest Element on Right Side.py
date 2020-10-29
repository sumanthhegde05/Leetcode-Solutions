class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr.reverse()
        right_max = -1
        prev_val = -1
        for item in range(len(arr)):
            right_max = max(right_max,prev_val)
            prev_val = arr[item]
            arr[item] = right_max
        arr.reverse()
        return arr
                