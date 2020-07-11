class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        a=[]
        minn=0
        maxx=len(S)
        for i in S:
            if i is "I":
                a.append(minn)
                minn+=1
            else:
                a.append(maxx)
                maxx-=1
        a.append(minn)
        return a
