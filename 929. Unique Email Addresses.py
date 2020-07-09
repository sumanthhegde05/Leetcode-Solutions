class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        p=[]
        for i in emails:
            a=i.split("@")
            b=''.join(a[0].split("."))
            c=''.join(b.split('+')[0])
            c=c+'@'+a[1]
            p.append(c)
        return len(set(p)) 
                
