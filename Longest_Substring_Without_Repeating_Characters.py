class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxx=0
        compare=[]
        if len(s)==0:
            return 0
        compare.append(s[0])
        for j in range(1,len(s)):
            if s[j] in compare:
                if len(compare)>maxx:
                    maxx=len(compare)
                del compare[:compare.index(s[j])+1]
            compare.append(s[j])
        if maxx<len(compare):
            maxx=len(compare)
        return maxx
            
            
