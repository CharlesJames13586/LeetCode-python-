class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for j in range(int(n/2)):
            for i in range(n-j*2-1):
                matrix[i+j][n-1-j], matrix[n-1-j][n-i-1-j], matrix[n-i-1-j][0+j],   matrix[0+j][i+j] = \
                matrix[0+j][i+j],   matrix[i+j][n-1-j],     matrix[n-1-j][n-i-1-j], matrix[n-i-1-j][0+j]


if __name__ == "__main__":
    solution = Solution()
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    # matrix = [[1]]
    matrix = [[1, 2], [3, 4]]
    solution.rotate(matrix)
    print(matrix)