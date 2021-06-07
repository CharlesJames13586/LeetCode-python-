class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_array = s.split(' ')
        while(len(s_array) > 0 and s_array[-1] == ''):
            s_array = s_array[:-1]
        else:
            if len(s_array) == 0:
                return 0
        return len(s_array[-1])


if __name__ == "__main__":
    Input = " "
    solution = Solution()
    print(solution.lengthOfLastWord(Input))