class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dictionary = {'U':1,
                      'D':-1,
                      'L':2,
                      'R':-2,}
        count=0
        for elem in moves:
            count+=dictionary[elem]
        if count==0:
            return True
        else:
            return False
