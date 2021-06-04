class Solution(object):
    def findNumbers(self, nums):
        self.count = 0
        
        for n in nums:
            string = str(n)
            self.count += 1 if len(string) % 2 == 0 else 0
            
        return self.count
        