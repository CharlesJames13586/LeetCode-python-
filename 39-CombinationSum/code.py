class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()                        # 对数据进行排序，方便提前退出
        result = []
        self.dfs(candidates, target, [], result)
        return result

    def dfs(self, candidates, target, path, result):
        """
        :param candidates:
        :param target:
        :param path: 记录临时结果
        :param result: 记录最终结果
        :return:
        """
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return
        for i in range(len(candidates)):
            if candidates[i] > target:           # 提高速度
                break
            self.dfs(candidates[i:], target - candidates[i], path + [candidates[i]], result)


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    solution = Solution()
    result = solution.combinationSum(candidates, target)
    print(result)