class Solution:
    def longestPalindrome(self, s: str) -> str:
        c=0
        ret=''
        for i in range (0,len(s)):
            for j in range (i+1,len(s)+1):
                if i<=j:
                    ss=s[i:j]
                    #print(ss)
                    y=ss[::-1]
                    if ss==y:
                        if len(ss)>c:
                            c = len(ss)
                            ret = ss[:]
        return ret
            
            
