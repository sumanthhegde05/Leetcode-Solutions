class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        a=text.split(" ")
        b=[]
        for i in range(0,(len(a)-2)):
            if a[i]==first:
                if second == a[i+1]:
                    b.append(a[i+2])
        return b
