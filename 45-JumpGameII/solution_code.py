class Solution(object):
    def jump(self, nums):
        """
        使用动态规划
        :type nums: List[int]
        :rtype: int
        """
        farthest = [0] * len(nums)
        numofjumps = [0] * len(nums)
        for i in range(len(nums)):
            farthest[i] = i + nums[i]
            if i > 0 and farthest[i] < farthest[i - 1]:
                farthest[i] = farthest[i - 1]
        point = len(nums) - 1
        for i in range(len(nums)):
            j = len(nums) - 1 - i
            if j < point:
                if farthest[j] < point:
                    point = j + 1
                numofjumps[j] = numofjumps[point] + 1

        return numofjumps[0]



if __name__ == "__main__":
    solution = Solution()
    nums = [2, 3, 1, 1, 4]
    print(solution.jump(nums))
    nums = [2, 3, 0, 1, 4]
    print(solution.jump(nums))