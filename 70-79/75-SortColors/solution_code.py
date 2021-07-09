class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        num_0 = 0
        num_1 = 0
        num_2 = 0
        for num in nums:
            if num == 0:
                num_0 = num_0 + 1
            elif num == 1:
                num_1 = num_1 + 1
            elif num == 2:
                num_2 = num_2 + 1

        # nums[0:num_0] = [0] * num_0
        # nums[num_0:num_0+num_1] = [1] * num_1
        # nums[num_0+num_1:num_0+num_1+num_2] = [2] * num_2
        for i in range(num_0):
            nums[i] = 0
        for i in range(num_1):
            nums[num_0+i] = 1
        for i in range(num_2):
            nums[num_0+num_1+i] = 2
        

if __name__ == "__main__":
    # nums = [2, 0, 2, 1, 1, 0]
    # nums = [2, 0, 1]
    nums = [0]
    solution = Solution()
    solution.sortColors(nums)
    print(nums)