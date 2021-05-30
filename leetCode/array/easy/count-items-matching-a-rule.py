class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        itemCount = {}
        index = 0
        
        if ruleKey == "color":
            index = 1
        if ruleKey == "name":
            index = 2
            
        for item in items:
            if item[index] not in itemCount:
                itemCount[item[index]] = 1
            else:
                itemCount[item[index]] += 1
        if ruleValue in itemCount:
            return itemCount[ruleValue]
        else:
            return 0