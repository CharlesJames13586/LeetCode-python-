class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        grid = [[0 for i in range(n)] for j in range(m)]
        grid[m-1][n-1] = 1
        if obstacleGrid[m-1][n-1] == 1:
            grid[m-1][n-1] = 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if grid[i][j] == 0:
                    if i + 1 < m:
                        grid[i][j] += grid[i+1][j]
                    if j + 1 < n:
                        grid[i][j] += grid[i][j+1]
                    if obstacleGrid[i][j] == 1:
                        grid[i][j] = 0
        return grid[0][0]


if __name__ == "__main__":
    # obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    obstacleGrid = [[0, 0], [0, 1]]
    solution = Solution()
    print(solution.uniquePathsWithObstacles(obstacleGrid))