class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        self.permute_search(nums, [], result)
        return result

    def permute_search_1(self, nums, path, result):
        if len(nums) == 0:
            if not path in result:
                result.append(path)
        else:
            for i in range(len(nums)):
                self.permute_search(nums[:i] + nums[i+1:], path + [nums[i]], result)

    def permute_search(self, nums, path, result):
        if len(nums) == 0:
            result.append(path)
        else:
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                self.permute_search(nums[:i] + nums[i+1:], path + [nums[i]], result)


if __name__ == "__main__":
    solution = Solution()
    # nums = [1, 1, 2]
    nums = [2,2,1,1]
    print(solution.permuteUnique(nums))