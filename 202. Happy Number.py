class Solution:
    def isHappy(self, n: int) -> bool:
        num=str(n)
        dictionay=[]
        while(len(num)>0):
            summ=0
            for i in num:
                summ+=int(i)**2
            if summ==1:
                return True
            if summ in dictionary:
                return False
            dictionary.append(summ)
            num=str(summ)
