class Solution(object):
    def checkZeroOnes(self, s):
        if len(s) < 2:
            return True if s == '1' else False
        long1 = 0
        long0 = 0
        maxLong1 = 0
        maxLong0 = 0
        
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                if s[i] == '1':
                    long1 += 1
                    if maxLong1 < long1:
                        maxLong1 = long1
                else:
                    long0 += 1
                    if maxLong0 < long0:
                        maxLong0 = long0
            else:
                long1 = 0
                long0 = 0
        return True if maxLong1 > maxLong0 else False