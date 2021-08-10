# 78. Subsets
Given an integer array `nums` of **unique** elements, return all possible subsets (the power set).

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

##### Example 1:
> **Input:** nums = [1,2,3]  
> **Output:** [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

---
##### 思路：
这个题是求所给集合的幂集的。

```python
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
```

1. 初始化一些变量

```python
        results = []
        # 空集是任何集合的子集
        results.append([])
        subset = []
```
results用来保存最终的结果，subset用来保存当前正在处理的子集。空集是任何集合的子集，所以将空集加入results中。

2. 搜索并返回

```python
        self.search(nums, 0, subset, results)
        return results
```

3. 搜索的过程

```python
    def search(self, nums, index, subset, results):
        for i in range(index, len(nums)):
            subset.append(nums[i])
            results.append(subset[:])
            self.search(nums, i+1, subset, results)
            del subset[-1]
```

这是一个递归搜索的过程，类似于一种深度优先的搜索吧。从index到nums的最后一个元素，将每个元素加入到subset中，然后向下一层搜索，下一层搜索是本层加入到subset中的元素后面的元素，这样可以避免出现重复的子集，每加一个元素，子集都变化了，所以要把它再加到results中，每次搜索回溯时，都要把加入的元素再删除掉。