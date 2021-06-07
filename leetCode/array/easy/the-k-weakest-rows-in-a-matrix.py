class Solution(object):
    def kWeakestRows(self, mat, k):
        rows = {}
        for i in range(len(mat)):
            total = 0
            for val in mat[i]:
                total += val
                
            if total in rows:
                rows[total] += [i]
            else:
                rows[total] = [i]
            
        sortRows = sorted(rows.keys())
        result = []
        for i in range(k):
            if i < len(sortRows) and sortRows[i] in rows:
                result += rows[sortRows[i]]
            
        return result[0:k]
        