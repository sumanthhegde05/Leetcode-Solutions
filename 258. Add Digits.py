class Solution:
    def addDigits(self, num: int) -> int:
        strnum = str(num)
        while(len(strnum)>1):
            summ=0
            for item in strnum:
                summ+=int(item)
            strnum=str(summ)
        return int(strnum)
