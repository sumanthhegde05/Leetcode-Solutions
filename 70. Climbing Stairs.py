class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return n
        temp1=1
        temp2=1
        for elem in range(2,n+1):
            temp1,temp2 = temp2, temp1+temp2
        return temp2
