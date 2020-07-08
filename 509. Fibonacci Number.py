class Solution:
    def fib(self, N: int) -> int:
        if N==0:
            return  0
        elif N<=2:
            return  1
        a=0
        b=1
        for elem in range(2,N+1):
            result = a+b
            a,b = b,result
        return  result
