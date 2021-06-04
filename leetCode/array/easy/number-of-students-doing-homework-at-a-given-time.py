class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        self.overlapTime = {}
        
        for i in range(len(startTime)):
            j = startTime[i]
            while j <= endTime[i]:
                if j not in self.overlapTime:
                    self.overlapTime[j] = 1
                else:
                    self.overlapTime[j] += 1
                j += 1
        return self.overlapTime[queryTime] if queryTime in self.overlapTime else 0
        