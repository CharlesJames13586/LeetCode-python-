# 73. Set Matrix Zeroes

Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s, and return the matrix.

You must do it in place.

##### Example 1:
![例1](./source/mat1.jpg)  
> **Input:** matrix = [[1,1,1],[1,0,1],[1,1,1]]  
> **Output:** [[1,0,1],[0,0,0],[1,0,1]]

##### Example 2:
![例2](./source/mat2.jpg)  
> **Input:** matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]  
> **Output:** [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

---
##### 思路：
遍历数组`matrix`，分开记录元素`0`所在的行和列，遍历完之后将对应行和列的元素全部置`0`即可，时间复杂度为O(n<sup>2</sup>)。详细细节可见代码。

```python
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row_coor = {}
        col_coor = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_coor[i] = True
                    col_coor[j] = True
        for row in row_coor.keys():
            for j in range(len(matrix[0])):
                matrix[row][j] = 0
        for col in col_coor.keys():
            for i in range(len(matrix)):
                matrix[i][col] = 0

        return matrix
```
