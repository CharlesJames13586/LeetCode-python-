class Solution(object):
    def isMatch(self, s, p):
        """
        普通的深度优先搜索
        这个答案会超时
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(s) == 0 and len(p) == 0:
            return True
        if len(p) > 0:
            if p[0] == '*':
                next = 1
                while next < len(p) and p[next] == '*':
                    next = next + 1
                for i in range(len(s) + 1):
                    if self.isMatch(s[i:], p[next:]):
                        return True
                return False
            elif p[0] == '?':
                if len(s) > 0:
                    return self.isMatch(s[1:], p[1:])
                elif len(s) == 0:
                    return False
            else:
                if len(s) > 0 and p[0] == s[0]:
                    return self.isMatch(s[1:], p[1:])
                else:
                    return False
        else:                                    # len(s) > 0
            return False

    def isMatch_1(self, s, p):
        """
        贪婪的深度搜索
        :type s: str
        :type p: str
        :return:
        """
        ss = ""
        star = ""
        while len(s) > 0:
            if len(p) > 0 and (p[0] == '?' or p[0] == s[0]):
                s = s[1:]
                p = p[1:]
                continue
            if len(p) > 0 and p[0] == '*':
                star = p
                p = p[1:]
                ss = s
                continue
            if len(star) > 0:          # 对'*'的通配，当上一个if走不通时，'*'的通配字符长度+1
                p = star[1:]
                s = ss[1:]
                ss = ss[1:]
                continue
            return False
        while len(p) > 0 and p[0] == '*':
            p = p[1:]
        return not len(p) > 0

    def isMatch_2(self, s, p):
        star_index = 0                           # 记录上一个'*'的位置
        p_index = 0                              # 记录p扫描的位置
        s_index = 0
        p_lenght = len(p)
        s_length = len(s)
        s_star_index = -1                        # s中与p中'*'匹配后的第一个字符的位置
        while s_index < s_length:                # s被匹配成功后截止
            # 匹配一个字符的情况
            if p_index < p_lenght and (p[p_index] == '?' or p[p_index] == s[s_index]):
                p_index = p_index + 1
                s_index = s_index + 1
                continue
            # '*'匹配情况
            if p_index < p_lenght and p[p_index] == '*':
                star_index = p_index             # 记录已扫描字符串中最后一个'*'的位置
                p_index = p_index + 1
                s_star_index = s_index           # 默认'*'匹配0个字符
                continue
            # 如果前两种情况都不成功，试着增加最后一个'*'匹配的字符串的长度
            if s_star_index != -1 and s_star_index < s_length:
                p_index = star_index + 1
                s_star_index = s_star_index + 1
                s_index = s_star_index
                continue
            # 如果都不成功，则宣告失败
            return False
        # 扫描p后多余的'*'
        while p_index < p_lenght and p[p_index] == '*':
            p_index = p_index + 1
        # 如果p未扫描结束，宣告失败
        return not p_index < p_lenght




if __name__ == "__main__":
    solution = Solution()
    s = "aa"; p = "a"
    # s = "aa"; p = "*"
    # s = "cb"; p = "?a"
    # s = "adceb"; p = "*a*b"
    # s = "acdcb"; p = "a*c?b"
    # s = ""; p = "?"
    # s = "babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb"
    # p = "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"
    # s = "abababba"
    # p = "a*ba"
    # print(solution.isMatch(s, p))
    print(solution.isMatch_2(s, p))
