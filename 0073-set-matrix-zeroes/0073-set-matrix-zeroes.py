class Solution(object):
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(n): 
                        if matrix[i][k] != 0: matrix[i][k] = 'x'
                    for l in range(m): 
                        if matrix[l][j] != 0: matrix[l][j] = 'x'
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'x': matrix[i][j] = 0


        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        