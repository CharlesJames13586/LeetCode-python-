import copy
class Solution(object):
    def __init__(self):
        self.result = []

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.result = []
        positions = [-1] * n                      # 使用一维数组存储第i行Q的位置
        self.solve(positions, 0)
        # 将self.result转化为所要求的输出
        answers = []
        for k in range(len(self.result)):
            answer = []
            for i in range(n):
                row = ""
                for j in range(n):
                    if self.result[k][i] == j:
                        row = row + 'Q'
                    else:
                        row = row + '.'
                answer.append(row)
            answers.append(answer)
        return answers

    def solve(self, positions, x):
        """
        使用递归的方式求解
        :param positions:
        :param x:
        :return:
        """
        n = len(positions)
        if x == n:                               # 当棋盘上的皇后数等于n时，找到一个解
            self.result.append(copy.deepcopy(positions))
            return
        else:
            for j in range(n):
                if self.check(positions, x, j):
                    positions[x] = j
                    self.solve(positions, x+1)
                    positions[x] = -1

    def check(self, positions, x, y):
        n = len(positions)
        if positions[x] > -1:
            return False
        for i in range(n):
            if positions[i] == y:
                return False
            if positions[i] > -1 and abs(i - x) == abs(positions[i] - y):
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.solveNQueens(4))
    print(solution.solveNQueens(1))