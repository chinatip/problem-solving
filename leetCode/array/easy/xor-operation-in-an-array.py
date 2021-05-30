class Solution(object):
    def xorOperation(self, n, start):
        self.value = 0
        if n == 1:
            return start
        
        for i in range(n):
            self.value = start + 2*i ^ self.value
        
        return self.value
        