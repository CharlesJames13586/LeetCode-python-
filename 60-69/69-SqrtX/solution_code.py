class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 二分法
        left = 0
        right = x
        middle = (left + right) // 2
        while left <= right:
            if (middle+1) * (middle+1) < x:
                left = middle
            elif middle * middle > x:
                right = middle
            elif middle * middle <= x and (middle+1) * (middle+1) > x:
                break
            elif (middle+1) * (middle+1) == x:
                middle += 1
                break
            middle = (left + right) // 2

        return middle



if __name__ == "__main__":
    solution = Solution()
    for x in range(100):
        print("sqrt({}) = {}".format(x, solution.mySqrt(x)))