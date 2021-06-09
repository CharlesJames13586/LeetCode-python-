# 63. Unique Paths II

A robot is located at the top-left corner of a `m x n` grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as `1` and `0` respectively in the grid.

##### Example 1:
![例1](./source/robot1.jpg)  
> **Input:** obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]  
> **Output:** 2  
> **Explanation:**  
> There is one obstacle in the middle of the 3x3 grid above.  
> There are two ways to reach the bottom-right corner:  
> 1. Right -> Right -> Down -> Down
> 2. Down -> Down -> Right -> Right

##### Example 2:
![例2](./source/robot2.jpg)  
> **Input:** obstacleGrid = [[0,1],[0,0]]  
> **Output:** 1 

---
##### 思路：
这道题只需要在[62题](../62-UniquePaths/solution_ideas.md)的基础上做略微改动就行，改动的地方有：  
1. 地图的大小不通过函数参数直接给定，而是从参数中的`obstacleGrid`矩阵中获得；
2. 每次在求得可抵达路径条数时，判断当前位置是否是障碍物，如果是的话，当前可抵达路径条数改为`0`,告知其它位置经由该位置不可抵达`Finsh`。