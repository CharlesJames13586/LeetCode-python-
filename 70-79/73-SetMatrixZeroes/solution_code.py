class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row_coor = {}
        col_coor = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_coor[i] = True
                    col_coor[j] = True
        for row in row_coor.keys():
            for j in range(len(matrix[0])):
                matrix[row][j] = 0
        for col in col_coor.keys():
            for i in range(len(matrix)):
                matrix[i][col] = 0

        return matrix


if __name__ == "__main__":
    # matrix = [[1,1,1],[1,0,1],[1,1,1]]
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    solution = Solution()
    print(solution.setZeroes(matrix))

        