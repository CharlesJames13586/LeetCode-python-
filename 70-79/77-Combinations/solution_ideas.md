# 77. Combinations

Given two integers `n` and `k`, return all possible combinations of `k` numbers out of the range `[1, n]`.

You may return the answer in **any order**.

##### Example 1:
> **Input:** n = 4, k = 2  
> **Output:**  
> [  
>  &nbsp;&nbsp;[2,4],  
>  &nbsp;&nbsp;[3,4],  
>  &nbsp;&nbsp;[2,3],  
>  &nbsp;&nbsp;[1,2],  
>  &nbsp;&nbsp;[1,3],  
>  &nbsp;&nbsp;[1,4],  
>]  

---
##### 思路：
这英文看了老半天都没理解，最后查了中文意思才明白。这个out让人很难理解。  
给定两个整数`n`和`k`，返回区间`[1,n]`中的`k`个整数组成的所有列表。

这道题我用的就是深度优先搜索，搜索k层，记录每层的数字，到第k层时将结果返回。每层只搜索上一层选中数字的后面的数字，这样就不用判断是否有重复的了，也可以说这是一种剪枝策略，甚至可以说使用这种搜索方法不用剪枝。

下面展示代码

```python
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
```

1. 初始化一些变量，调用DFS，返回结果。

```python
        combination = [0] * k
        results = []
        self.DFS(0, 0, n, k, combination, results)

        return results
```

combination记录的是当前收集的整数，results记录的是第k层收集完成后combination中的排列。

2. DFS

```python
    def DFS(self, now, all, n, k, combination, results):
        if all == k:
            # results.append(combination.copy())
            results.append(combination[:])
            return
        for j in range(now, n):
            combination[all] = j + 1
            self.DFS(j+1, all+1, n, k, combination, results)
            combination[all] = 0
```

all表示当前combination中已经有的数字的个数。当all为k时，将结果记录在results中，然后返回。
for循环遍历now到n的数字，每层都这么只遍历now及后面的，然后调用DFS时，将now加1，这样就只向前走，不需要剪枝了。