class Solution:
    def reverse(self, x: int) -> int:
        y=0
        while True:
            if x>0:
                y=y+int(x%10)
            else:
                y=y+int(x%-10)
            x=int(x/10)
            if x == 0:
                break
            y=y*10  
        if y>(2**31)-1 or y<(-2**31):
            return 0
        else:
            return y
