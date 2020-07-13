class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictionary={'2':'abc',
                   '3':'def',
                   '4':'ghi',
                   '5':'jkl',
                   '6':'mno',
                   '7':'pqrs',
                   '8':'tuv',
                   '9':'wxyz',
                  }
        result=[]
        def recur(combination,digits):
            if len(digits)==0:
                if combination!='':
                    result.append(combination)
            else:
                for item in dictionary[digits[0]]:
                    recur(combination+item,digits[1:])
        recur('',digits)
        return result
                
