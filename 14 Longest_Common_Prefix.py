class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if (len(strs)>1):
            save=strs[0]
            for i in range(1,len(strs)):
                temp=''
                for j in range(0,min(len(save),len(strs[i]))):
                    if save[j]==strs[i][j]:
                        temp=temp+save[j]
                    else:
                        break
                save=temp
        elif (len(strs)==1):
            temp=strs[0]
        else:
            temp=""
        return temp
