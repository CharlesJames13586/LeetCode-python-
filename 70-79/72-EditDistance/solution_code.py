class Solution(object):
    # 递归的方法会超时
    def minDistanceByRecursive(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # 如果word1或word2为空
        if word1 == "":
            return len(word2)
        if word2 == "":
            return len(word1)
        
        # 如果word1[0] == word2[0]
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        # 如果 word1[0] != word2[0]
        else:
            # 在word1前插入word2[0]
            insert = 1 + self.minDistance(word1, word2[1:])
            # 删除word1[0]
            delete = 1 + self.minDistance(word1[1:], word2)
            # 用替换word1[0]替换word2[0]
            replace = 1 + self.minDistance(word1[1:], word2[1:])

            return min(insert, delete, replace)

    # 动态规划做法
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        num1 = len(word1)
        num2 = len(word2)

        memo = [[0] * (num1+1) for i in range(num2+1)]
        
        for i in range(num2, -1, -1):
            for j in range(num1, -1, -1):
                if j == num1:
                    memo[i][j] = num2 - i
                    continue
                if i == num2:
                    memo[i][j] = num1 - j
                    continue
                
                if word1[j] == word2[i]:
                    memo[i][j] = memo[i+1][j+1]
                else:
                    insert = 1 + memo[i][j+1]
                    delete = 1 + memo[i+1][j]
                    replace = 1 + memo[i+1][j+1]
                    memo[i][j] = min(insert, delete, replace)
        # memo[i][j] = max(memo[1][0], memo[0][1])
        return memo[0][0]



if __name__ == "__main__":
    # word1 = "horse"
    # word2 = "ros"
    word1 = "intention"
    word2 = "execution"
    solution = Solution()
    print(solution.minDistance(word1, word2))