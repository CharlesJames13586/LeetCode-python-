# 90. Subsets II
Given an integer array `nums` that may contain duplicates, return all posible subsets (the power set). The solution set **must not** contain duplicate subsets. Return the solution in any order.

### Example 1:
> **Input:** nums = [1,2,2]  
> **Output:** [[],[1],[1,2],[1,2,2],[2],[2,2]]

### Constraints:
* `1 <= nums.length <= 10`
* `-10 <= nums[i] <= 10`

---
### 思路
求一个集合的幂集，这里给出两种方式：  
1. 使用二进制表示法，使用长度与集合元素个数的二进制数，每一位表示一个元素，0表示不选取，1表示选取，将所有二进制数代表集合依次输出即可。
2. 使用递归方法，将空集放入（结果）集合，然后依次往（结果）集合中每一个元素（也是一个集合）放入原集合的每一个元素，直到添加完毕。

不过本题原集合中有重复的元素，要求返回结果的集合不能包含相同的元素。因此建议采用第二个方法，提前将原集合排序，这样在放入元素时跳过相同的元素即可。