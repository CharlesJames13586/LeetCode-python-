class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = len(s)
        n = len(t)
        
        s_sub = []
        s_pos = []
        for i in range(m):
            if s[i] in t:
                s_sub.append(s[i])
                s_pos.append(i)

        # 给t搞个字典
        t_dict = {}
        t_num = 0            # 用来同步t中未匹配剩余字符的个数
        for key in t:
            if key not in t_dict.keys():
                t_dict[key] = 1
            else:
                t_dict[key] += 1
            t_num += 1
        
        t_num_dup = 0        # 记录多匹配字符的个数
        left = 0             # 记录滑动窗口左侧的位置
        old_left = 0
        minwindow = m + 1
        windowLenght = m + 1
        # 开始遍历
        for i in range(len(s_sub)):
            if t_dict[s_sub[i]] > 0:
                t_dict[s_sub[i]] -= 1
                t_num -= 1
            elif t_dict[s_sub[i]] <= 0:
                t_dict[s_sub[i]] -= 1
                t_num_dup += 1

            while t_num == 0:     # 说明找齐了，使用wihle循环是因为可能要右移好几个重复的字符串
                windowLenght = s_pos[i] - s_pos[left] + 1
                if windowLenght < minwindow:
                    old_left = left
                    minwindow = windowLenght
                    if minwindow == n:      # 因为只有1个解，所以当找到最少的窗口时，可以跳出循环
                        break
                # 窗口右滑1个字符
                if t_dict[s_sub[left]] == 0:
                    t_dict[s_sub[left]] += 1
                    t_num += 1
                elif t_dict[s_sub[left]] < 0:
                    t_dict[s_sub[left]] += 1
                    t_num_dup -= 1
                
                left += 1     

 
        if minwindow == m + 1:    # 说明没有最小窗口
            return ""
        elif minwindow < m + 1:
            return s[s_pos[old_left]: s_pos[old_left] + minwindow]

        



if __name__ == "__main__":
    solution = Solution()
    # s = "ADOBECODEBANC"
    # t = "ABC"
    # s = "a"
    # t = "a"
    # s = "a"
    # t = "aa"
    s = "cabwefgewcwaefgcf"
    t = "cae"
    print(solution.minWindow(s, t))