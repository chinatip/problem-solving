class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxCandies = 0
        result = []
        for c in candies:
            if c > maxCandies:
                maxCandies = c
        
        for c in candies:
            result += [True] if (c + extraCandies >= maxCandies) else [False]
        return result