class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count=0
        a=""
        for i in range (0,len(S)):
            if(S[i]=='('):
                count = count+1
                if(count>1):
                    a=a+"("
            else:
                count = count-1
                if(count!=0):
                    a=a+")"
        return a
