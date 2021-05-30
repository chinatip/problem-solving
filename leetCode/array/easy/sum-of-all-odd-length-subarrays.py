class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        sum = 0
        l = 1
        while l <= len(arr):
            if l % 2 == 0:
                l += 1
                continue
            for i in range(len(arr)):
                lineSum = 0
                for loop in range(l):
                    if i + loop >= len(arr):
                        lineSum = 0
                        continue
                    lineSum += arr[i + loop]
                sum += lineSum
            l += 1
        return sum