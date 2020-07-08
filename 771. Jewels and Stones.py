class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for i in J:
            for k in S:
                if i is k:
                    count+=1
        return count
