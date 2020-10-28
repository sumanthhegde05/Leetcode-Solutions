class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        first=1
        second=1
        table=[first,second]
        while True:
            res=first+second
            if res>k:
                break
            table.append(res)
            first=second
            second=res
        table.reverse()
        count=0
        for item in table:
            if item <= k:
                count+=1
                k-=item
        return count