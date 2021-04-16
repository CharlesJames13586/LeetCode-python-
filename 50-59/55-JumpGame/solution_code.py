class Solution(object):
    def canJump(self, nums):
        """
        从最后一个元素，
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        goal = n - 1
        for i in range(n)[::-1]:
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False


    def canJump_1(self, nums):
        """
        从最后一个元素，开始标记可以到达最后一位的元素，依次向前标记
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        labels = ['N']*n               # 标签数组，'J'代表可以跳到最后一个位置，'N'代表不可以
        labels[n-1] = 'J'              # 初始化最后一个元素可以跳到自身
        for i in range(n):
            self.label(n-1-i, nums, labels)
        return True if labels[0] == 'J' else False

    def label(self, index, nums, labels):
        if index < len(nums)-2:
            if nums[index] <= nums[index+1]+1 and labels[index+1] != 'J':
                # 如果下一个跳不到最后一个元素，并且当前元素的值+1不大于下一个元素的值，
                # 则当前元素也跳到不到最后一个元素
                return
        for i in range(nums[index]+1):
            if labels[index + i] == 'J':
                labels[index] = 'J'
                break
        return


if __name__ == "__main__":
    solution = Solution()
    nums = [2, 3, 1, 1, 4]
    # nums = [3, 2, 1, 0, 4]
    # nums = [5, 4, 3, 2, 1, 0, 0]
    print(solution.canJump(nums))

