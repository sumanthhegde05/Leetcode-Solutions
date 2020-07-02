class Solution:
    def isValid(self, s: str) -> bool:
        k=[]
        flag=False
        if s is "":
            flag = True
        for i in s:
            if i=='(' or i=='{' or i=='[':
                k.append(i)
            else:
                if i == ')' and k !=[] :
                    if k.pop() == '(':
                        flag = True
                    else:
                        flag=False
                        break
                elif i ==']' and k !=[] :
                    if k.pop() == '[':
                        flag = True
                    else:
                        flag = False
                        break
                elif i == '}' and k !=[]: 
                    if k.pop() == '{':
                        flag = True
                    else:
                        flag = False
                        break
                else:
                    flag = False
                    break
        if k !=[]:
            flag = False
        return flag
