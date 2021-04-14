class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        self.curDireIndex = 0
        self.Direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m = len(matrix)
        n = len(matrix[0])
        SpiralMatrix = [[0 for i in range(n)] for j in range(m)]

        row = 0
        col = 0
        result = []
        for i in range(m):
            for j in range(n):
                result.append(matrix[row][col])
                SpiralMatrix[row][col] = 1
                row, col = self.next(row, col, SpiralMatrix)

        return result


    def next(self, i, j, SpiralMatrix):
        m = len(SpiralMatrix)
        n = len(SpiralMatrix[0])
        next_i = i + self.Direction[self.curDireIndex][0]
        next_j = j + self.Direction[self.curDireIndex][1]
        if next_i < m and next_j < n and SpiralMatrix[next_i][next_j] == 0:
            pass
        else:
            self.curDireIndex = (self.curDireIndex + 1) % 4
            next_i = i + self.Direction[self.curDireIndex][0]
            next_j = j + self.Direction[self.curDireIndex][1]
        return next_i, next_j


if __name__ == "__main__":
    solution = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    # matrix = [[1]]
    print(solution.spiralOrder(matrix))