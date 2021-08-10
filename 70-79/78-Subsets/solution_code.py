class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        # 空集是任何集合的子集
        results.append([])
        subset = []
        self.search(nums, 0, subset, results)
        return results

    def search(self, nums, index, subset, results):
        for i in range(index, len(nums)):
            subset.append(nums[i])
            results.append(subset[:])
            self.search(nums, i+1, subset, results)
            del subset[-1]



if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.subsets(nums))