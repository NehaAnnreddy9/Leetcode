class Solution(object):
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0: return False
        left = 0
        right = (len(matrix) * len(matrix[0])) - 1
        ln = len(matrix[0])
        while left <= right:
            middle = (left+right) // 2
            potentialMatch = matrix[middle // ln][middle % ln]
            if target == potentialMatch:
                return True
            elif target < potentialMatch:
                right = middle - 1
            else:
                left = middle + 1
        return False
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        