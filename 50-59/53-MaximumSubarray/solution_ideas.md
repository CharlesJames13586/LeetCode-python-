# 53. Maximum Subarray
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum
and return its sum.

##### Example 1:
> **Input:** nums = [-2,1,-3,4,-1,2,1,-5,4]  
> **Output:** 6  
> **Explanation:** [4,-1,2,1] has the largest sum = 6.

---
##### 思路：
这是一个求数组最大连续子数组的和，是一个很经典的题，也是一个easy难度的题。从前往后扫描，累加每个元素到sum上，如果sum变为
负数，置零，重新开始累加。在累加过程中保存最大值即可。
不同的是，这道题要求子数组最少包含一个元素，这样当最大值求的数为0时，说明原数组的数可能都为负数，这时输出数组中最大的数即可。