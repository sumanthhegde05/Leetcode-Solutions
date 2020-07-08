class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        num = str(bin(n)).split('0b')
        for elem in range(0,len(num[1])-1):
            print((int(num[1][elem+1])+1)%2)
            if int(num[1][elem])==(int(num[1][elem+1])+1)%2:
                pass
            else:
                return False
        return True
            
            
