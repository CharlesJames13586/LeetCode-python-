class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 还是要动态规划，这几道都是动态规划
        memo = [0] * n
        # 初始化两个值
        if n >= 1:
            memo[-1] = 1
        if n >= 2:
            memo[-2] = 2
        for i in range(n-3, -1, -1):
            memo[i] = memo[i+1] + memo[i+2]
        
        return memo[0]
        