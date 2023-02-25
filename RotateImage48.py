class Solution(object):
    def rotate(self, matrix):
        i = j = len(matrix)
        if i == 1: return matrix
        swaps = i//2
        for l in range(j):
            for s in range(swaps):
                matrix[s][l],matrix[j-1-s][l] = matrix[j-1-s][l],matrix[s][l]
        for k in range(i):
            for l in range(k,j):
                matrix[k][l], matrix[l][k] = matrix[l][k], matrix[k][l]
        return matrix
