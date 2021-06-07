class Solution(object):
    def heightChecker(self, heights):
        expHeights = sorted(heights)
        countDiff = 0
        for i in range(len(heights)):
            countDiff += 1 if heights[i] != expHeights[i] else 0
            
        return countDiff
        