class Solution(object):
    def finalPrices(self, prices):
        self.result = prices[:]
        for i in range(len(prices)):
            if i == len(prices) - 1:
                break
            j = i + 1
            while j < len(prices):
                if prices[i] >= prices[j]:
                    self.result[i] -= prices[j]
                    break
                j += 1
        return self.result