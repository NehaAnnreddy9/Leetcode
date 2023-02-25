class Solution(object):
    def spiralOrder(self, matrix):
        i = len(matrix)
        j = len(matrix[0])
        i_low = j_low = 0
        arr = []
        while(True):
            if i_low == i or j_low == j: break
            if i_low == i-1:
                for l in range(j_low,j):
                    arr.append(matrix[i-1][l])
                break
            elif j_low == j-1:
                for k in range(i_low,i):
                    arr.append(matrix[k][j-1])
                break
            else:
                for l in range(i_low,j-1):
                    arr.append(matrix[i_low][l])
                for k in range(i_low,i-1):
                    arr.append(matrix[k][j-1])
                for l in range(j-1,j_low,-1):
                    arr.append(matrix[i-1][l])
                for k in range(i-1,j_low,-1):
                    arr.append(matrix[k][j_low])
            i_low = j_low = i_low + 1
            i-=1
            j-=1

        return arr
