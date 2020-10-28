class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dictionary={}
        for item in paths:
            if item[1] not in dictionary.keys():
                dictionary[item[1]] = False
            if item[0] not in dictionary.keys():
                dictionary[item[0]] = False
            if item[0] in dictionary.keys():
                dictionary[item[0]] = True
                
        for item in dictionary.keys():
            if dictionary[item] == False:
                return item
        