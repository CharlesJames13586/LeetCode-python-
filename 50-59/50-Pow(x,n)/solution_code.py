class Solution(object):
    def __init__(self):
        self.result = {}

    def myPow(self, x, n):
        print("正在计算pow({}, {})".format(x, n))
        if n == 0:
            return 1.0
        elif n == 1:
            return x
        elif n == -1:
            return 1/x

        if n % 2 == 1:
            return x * self.myPow(x, n//2)**2
        else:
            return self.myPow(x, n//2)**2

    def myPow_1(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        self.result = {0:1}

        # 递归调用在n很大时容易造成递归深度超限
        # 修改后又造成了遍历数太大
        # 使用动态规划试一试吧
        # 记得每次外部调用都要清空result
        if n > 0:
            return self.powWithPositiveExp(x, n)
        elif n == 0:
            return 1
        elif n < 0:
            return 1 / self.powWithPositiveExp(x, -n)

    def powWithPositiveExp(self, x, n):
        print("正在计算pow({}, {})".format(x, n))
        if n in self.result:
            return self.result[n]
        pow1 = self.powWithPositiveExp(x, (n - 1) // 2)
        pow2 = self.powWithPositiveExp(x, n - 1 - (n - 1) // 2)
        self.result[(n - 1) // 2] = pow1
        self.result[n - 1 - (n - 1) // 2] = pow2
        return x * pow1 * pow2




if __name__ == "__main__":
    solution = Solution()
    print(solution.myPow(2.1, 3))
    print(solution.myPow(0.00001, 2147483647))