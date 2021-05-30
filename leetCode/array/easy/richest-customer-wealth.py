class Solution(object):
    def maximumWealth(self, accounts):
        highestAmount = 0
        for acc in accounts:
            sum = 0
            for a in acc:
                sum += a
                
            highestAmount = sum if sum > highestAmount else highestAmount
            
        return highestAmount