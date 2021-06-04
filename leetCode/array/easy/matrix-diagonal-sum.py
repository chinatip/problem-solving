class Solution(object):
    def diagonalSum(self, mat):
        diagonalSum = 0
        for i in range(len(mat)):
            diagonalSum += mat[i][i]
            if i != (len(mat) - i - 1):
                diagonalSum += mat[i][len(mat) - i - 1]
        return diagonalSum

        