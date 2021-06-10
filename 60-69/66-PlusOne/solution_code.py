class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0       # 进位
        result = [0] * len(digits)
        for i in range(len(digits)-1, -1, -1):
            if i == len(digits) - 1:
                result[i] = digits[i] + 1
            else:
                result[i] = digits[i]
            result[i] += carry
            if result[i] >= 10:
                carry = result[i] // 10
                result[i] = result[i] % 10
            else:
                carry = 0
        if carry > 0:
            result = [carry] + result
        return result


if __name__ == "__main__":
    # digits = [4, 3, 2, 1]
    # digits = [1, 2, 3]
    # digits = [0]
    digits = [9, 9, 9]
    solution = Solution()
    print(solution.plusOne(digits))