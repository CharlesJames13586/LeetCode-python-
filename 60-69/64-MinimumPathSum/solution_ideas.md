# 64. Minimum Path Sum

Given a `m x n` `grid` filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

**Note:** You can only move either down or right at any point in time.

##### Example 1:
![例1](./source/minpath.jpg)  
> **Input:** grid = [[1,3,1],[1,5,1],[4,2,1]]  
> **Output:** 7  
> **Explanation:** Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

---
##### 思路：
依旧使用动态规划
从后往前扫描，每个位置的最短路径和等于右侧和下侧的最短路径和较小的那个加上当前位置的权重。  
需要注意的是 `right_sum` 和 `down_sum` 的初值应为正无穷，但是python的整数没有正无穷大，所以根据约束条件赋值为`200 * 200 * 100 + 1`，刚开始赋值为`101`，最后两个用例因为值太大，一直ac不了，花了不少时间才找到这个bug。

```python
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
```
