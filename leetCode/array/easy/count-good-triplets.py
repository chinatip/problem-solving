class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        count = 0
        for i in range(len(arr) - 2):
            j = i + 1
            while j < len(arr) - 1:
                k = j + 1
                while k < len(arr):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count +=1
                    k += 1
                j += 1

        return count
        