class Solution(object):
    def sumZero(self, n):
        self.arr = []
        for i in range(n):
            if i < n // 2:
                self.arr += [n//2-i]
                continue
            if n % 2 != 0:
                if n // 2 == i:
                    self.arr += [0]
                    continue
                self.arr += [n//2 - i]
            else:
                self.arr += [n//2 - i - 1]
        return self.arr
        