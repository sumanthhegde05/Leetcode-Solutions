class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s1 = 'qwertyuiopQWERTYUIOP'
        s2 = 'asdfghjklASDFGHJKL'
        s3 = 'zxcvbnmZXCVBNM'
        
        a = {i: 1 for i in s1}
        b = {i: 1 for i in s2}
        c = {i: 1 for i in s3}
        d=[]
        for word in words:
            if all(char in a for char in word):
                        d.append(word)
            elif all(char in b for char in word):
                        d.append(word)
            elif all(char in c for char in word):
                        d.append(word)
        return d
