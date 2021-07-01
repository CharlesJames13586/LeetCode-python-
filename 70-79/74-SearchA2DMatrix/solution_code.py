class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 寻找target所在行
        up = 0
        down = len(matrix) - 1
        row = (up + down) // 2

        while up <= down:
            if matrix[row][0] < target:
                if row + 1 < len(matrix):
                    if matrix[row+1][0] < target:
                        up = row + 1
                    elif matrix[row+1][0] == target:
                        return True
                    elif matrix[row+1][0] > target:
                        break
                else:
                    break
            elif matrix[row][0] == target:
                break
            elif matrix[row][0] > target:
                down = row - 1

            row = (up + down) // 2

        # 寻找所在列
        left = 0
        right = len(matrix[0]) - 1
        col = (left + right) // 2

        while left <= right:
            if matrix[row][col] < target:
                left = col + 1
            elif matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = col -1
            col = (left + right) // 2
        return False


if __name__ == "__main__":
    solution = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    # matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    # target = 13
    # matrix = [[1]]
    # target = 2
    print(solution.searchMatrix(matrix, target))