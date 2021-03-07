class Solution(object):
    def combinationSum2(self, candidates, target):
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
            if not path in result :
                result.append(path)
            return
        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > target:           # 提前退出，剪枝提高速度
                break
            self.dfs(candidates[i + 1:], target - candidates[i], path + [candidates[i]], result)


if __name__ == "__main__":
    candidates = [10,1,2,7,6,1,5]
    target = 8
    solution = Solution()
    result = solution.combinationSum2(candidates, target)
    print(result)