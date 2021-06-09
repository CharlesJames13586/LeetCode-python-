class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 动态规划
        grid = [[0 for i in range(n)] for j in range(m)]
        grid[m-1][n-1] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if grid[i][j] == 0:
                    if i + 1 < m:
                        grid[i][j] += grid[i+1][j]
                    if j + 1 < n:
                        grid[i][j] += grid[i][j+1]
        return grid[0][0]


if __name__ == "__main__":
    m = 3
    n = 7
    solution = Solution()
    print(solution.uniquePaths(m, n))