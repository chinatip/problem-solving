class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        result = 0
        for i in range(1, len(points)):
            lastPoint = points[i-1]
            currentPoint = points[i]
            diffX = abs(lastPoint[0] - currentPoint[0])
            diffY = abs(lastPoint[1] - currentPoint[1])
            result += diffX if diffX > diffY else diffY
        return result