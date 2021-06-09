class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        memo = [[0 for i in range(n)] for j in range(m)]
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    memo[i][j] = grid[i][j]
                    continue
                right_sum = 200 * 200 * 100 + 1        # 题目中的约束条件显示grid中的值在[0,100]区间内,n和m在[1,200]
                down_sum = 200 * 200 * 100 + 1
                if i + 1 < m:
                    down_sum = memo[i+1][j]
                if j + 1 < n:
                    right_sum = memo[i][j+1]
                memo[i][j] = min(right_sum, down_sum) + grid[i][j]
        
        return memo[0][0]

if __name__ == "__main__":
    Grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    # Grid = [[1, 2, 3], [4, 5, 6]]
    solution = Solution()
    print(solution.minPathSum(Grid))
