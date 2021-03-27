class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.permute_serch(nums, [], result)
        return result

    def permute_serch(self, nums, path, result):
        if len(nums) == 0:
            result.append(path)
        else:
            for i in range(len(nums)):
                self.permute_serch(nums[:i] + nums[i+1:], path + [nums[i]], result)


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.permute(nums))