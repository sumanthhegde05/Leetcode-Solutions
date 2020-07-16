class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ptr = len(digits)-1
        while ptr>=0:
            digits[ptr]+=1
            if digits[ptr]>9:
                carry=1
                digits[ptr]=0
            else:
                return digits
            ptr-=1
        digits.insert(0,1)
        return digits
