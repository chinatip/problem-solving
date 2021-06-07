class Solution(object):
    def replaceElements(self, arr):
        curMax = 0
        result = []
        for i in reversed(range(len(arr))):
            if i == len(arr) -1:
                curMax = arr[i]
                result = [-1]
            else:
                result = [curMax] + result
                if arr[i] > curMax:
                    curMax = arr[i]
                    
        return result