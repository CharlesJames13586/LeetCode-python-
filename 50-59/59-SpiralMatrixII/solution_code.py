class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.curDireIndex = 0
        self.Direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        matrix = [[0] * n for i in range(n)]

        row = 0
        col = 0
        curNum = 1
        for i in range(n * n):
            matrix[row][col] = curNum
            row, col = self.next(row, col, matrix)
            curNum += 1
        return matrix

    def next(self, i, j, matrix):
        n = len(matrix)
        next_i = i + self.Direction[self.curDireIndex][0]
        next_j = j + self.Direction[self.curDireIndex][1]

        if next_i < n and next_j < n and matrix[next_i][next_j] == 0:
            pass
        else:
            self.curDireIndex = (self.curDireIndex + 1) % 4
            next_i = i + self.Direction[self.curDireIndex][0]
            next_j = j + self.Direction[self.curDireIndex][1]
        return next_i, next_j
        

if __name__ == "__main__":
    Input = 3
    solution = Solution()
    print(solution.generateMatrix(Input))