class Solution(object):
    def largestAltitude(self, gain):
        lastAltitude = 0
        highestAltitude = 0
        
        for h in gain:
            currentAltitude = lastAltitude + h
            if highestAltitude < currentAltitude:
                highestAltitude = currentAltitude
            lastAltitude = currentAltitude
        return highestAltitude
                
        