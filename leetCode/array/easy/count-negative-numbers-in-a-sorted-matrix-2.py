class Solution(object):
    def countNegatives(self, grid):
        self.arr = []
        for row in grid:
            self.arr += row
        grid = []
        for val in self.arr:
            if val < 0:
                grid += [val]
        return len(grid)