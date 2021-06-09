class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if s == "":
            return False
        # 检查符号'+'和'-'
        if s != "" and s[0] in ['+', '-']:
            s = s[1:]
        # 检查数字
        preDot = False
        preE = False
        while s != "" and s[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            preE = True
            preDot = True
            s = s[1:]
        # 检查小数点和小数位的数
        afterDot = False
        if s != "" and s[0] == '.':
            preE = True
            s = s[1:]
            while s != "" and s[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                afterDot = True
                s = s[1:]
            # 如果存在'.'，但小数点前后都没有数字，则返回False
            if not preDot and not afterDot:
                return False
        # 检查'e'或'E'和之后的数字
        afterE = False
        if preE and s != "" and s[0] in ['e', 'E']:
            s = s[1:]
            # 检查符号'+'和'-'
            if s != "" and s[0] in ['+', '-']:
                s = s[1:]
            while s != "" and s[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                afterE = True
                s = s[1:]
            if afterE == False:
                return False
        if s == "":
            return True
        else:
            return False


if __name__ == "__main__":
    s = "005047e+6"
    solution = Solution()
    print(solution.isNumber(s))