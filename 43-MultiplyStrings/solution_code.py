class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(eval(num1 + '*' + num2))


if __name__ == "__main__":
    solution = Solution()
    num1 = "123"
    num2 = "456"
    print(solution.multiply(num1, num2))