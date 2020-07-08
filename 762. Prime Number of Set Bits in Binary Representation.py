class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        prime = {2, 3, 5, 7, 11, 13, 17, 19}
        total_count = 0
        for i in range(L, R+1):
            count = bin(i).count('1')
            if count in prime:
                total_count +=1
        return total_count
