class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        orderedNums = nums
        orderedNums.sort()
        index = 0
        positiveInteger = 1
        while True:
            while index < len(orderedNums) and orderedNums[index] < positiveInteger:
                index = index + 1
            if index >= len(orderedNums) :
                return positiveInteger
            else:
                if orderedNums[index] == positiveInteger:
                    positiveInteger = positiveInteger + 1
                elif orderedNums[index] > positiveInteger:
                    return positiveInteger

    def firstMissingPositive2(self, nums):
        nums.sort()
        positiveInteger = 1
        while positiveInteger in nums:
            positiveInteger = positiveInteger + 1

        return positiveInteger


if __name__ == "__main__":
    solution = Solution()
    nums = [3,4,-1,1]
    print(solution.firstMissingPositive2(nums))
