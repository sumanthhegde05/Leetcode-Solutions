class Solution:
    def myAtoi(self, Str: str) -> int:
        Str = Str.strip(" ")
        num=0
        if (len(Str)):
            a={
                '1':1,
                '2':2,
                '3':3,
                '4':4,
                '5':5,
                '6':6,
                '7':7,
                '8':8,
                '9':9,
                '0':0,
            }
            if Str[0]=='-' or Str[0]=='+':
                for char in range(1,len(Str)):
                    try:
                        num=(num*10)+a[Str[char]]
                    except:
                        break
                if Str[0]=="-":
                    num*=-1
           
            else:
                for char in Str:
                    try:
                        num=(num*10)+a[char]

                    except:
                        break
            if num<(-(2**31)):
                return -2**31
            elif num>((2**31)-1):
                return (2**31)-1
        return num
