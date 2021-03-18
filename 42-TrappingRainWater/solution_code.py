class Solution(object):
    def trap(self, height):
        """
        暴力解法：正确，但是倒数第二个用例未通过，超时
        :type height: List[int]
        :rtype: int
        """
        heightOfWater = 1
        columeOfWater = 0
        flagOfOver = False
        while not flagOfOver:
            flagOfOver = True
            left = -1
            right = -1
            for i in range(len(height)):
                if height[i] > heightOfWater:
                    flagOfOver = False
                if left == -1:
                    if height[i] >= heightOfWater:
                        left = i
                elif left != -1:
                    if height[i] >= heightOfWater:
                        right = i
                        columeOfWater = columeOfWater + right - left - 1
                        left = right
            heightOfWater = heightOfWater + 1

        return columeOfWater

    def trap_2(self, height):
        columeOfWater = 0
        lMax = 0
        rMax = 0
        left = 0
        right = len(height) - 1
        while left < right:
            lMax = max(lMax, height[left])
            rMax = max(rMax, height[right])
            if height[left] < height[right]:
                if height[left] < lMax:
                    columeOfWater = columeOfWater + lMax - height[left]
                left = left + 1
            else:
                if height[right] < rMax:
                    columeOfWater = columeOfWater + rMax - height[right]
                right = right - 1

        return columeOfWater


if __name__ == "__main__":
    solution = Solution()
    # height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    height = [4, 2, 0, 3, 2, 5]
    # height = [4, 2, 3]
    print(solution.trap_2(height))