class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        length = max(len(a), len(b))
        if len(a) < length:
            a = '0' * (length - len(a)) + a
        if len(b) < length:
            b = '0' * (length - len(b)) + b
        carry = 0
        c = ['0'] * length
        for i in range(length - 1, -1, -1):
            result = int(a[i]) + int(b[i]) + carry
            if result < 2:
                c[i] = str(result)
                carry = 0
            else:
                c[i] = str(result % 2)
                carry = result // 2
        if carry == 1:
            c = ['1'] + c
        c = ''.join(c)
        return c



if __name__ == "__main__":
    # a = "11"
    # b = "1"
    a = "1010"
    b = "1011"
    solution = Solution()
    print(solution.addBinary(a, b))