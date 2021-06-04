class Solution(object):
    def countNegatives(self, grid):
        self.countNeg = 0
        self.arr = []
        for row in grid:
            self.arr += row
        
        for val in self.arr:
            if val < 0:
                self.countNeg += 1
        return self.countNeg