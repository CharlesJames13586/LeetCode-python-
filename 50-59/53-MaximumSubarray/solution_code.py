class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        Max = 0
        for i in nums:
            sum = sum + i
            if sum < 0:
                sum = 0 if i < 0 else i
            if sum > Max:
                Max = sum
        if Max == 0:
            Max = max(nums)
        return Max

    def maxSubArray_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        max = nums[0] if len(nums) > 0 else 0
        head = 0
        for i in nums:
            sum = sum + i
            if sum < 0 or head < 0:
                sum = i
                head = i
            if sum > max:
                max = sum
        return max


if __name__ == "__main__":
    solution = Solution()
    # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # nums = [1]
    # nums = [5, 4, -1, 7, 8]
    nums = [-1]
    print(solution.maxSubArray(nums))