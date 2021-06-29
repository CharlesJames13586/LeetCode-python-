# 72. Edit Distance

Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`.

You have the following three operations permitted on a word:

* Insert a character
* Delete a character
* Replace a character

##### Example 1:
> **Input:** word1 = "horse", word2 = "ros"  
> **Output:** 3  
> **Explanation:**  
> horse -> rorse (replace 'h' with 'r')  
> rorse -> rose (remove 'r')  
> rose -> ros (remove 'e')

##### Example 2:
> **Input:** word1 = "intention", word2 = "execution"  
> **Output:** 5  
> **Explanation:**  
> intention -> inention (remove 't')  
> inention -> enention (replace 'i' with 'e')  
> enention -> exention (replace 'n' with 'x')  
> exention -> exection (replace 'n' with 'c')  
> exection -> execution (insert 'u')


---
##### 思路
这是一道求两个单词之间最小修改次数的题，修改方式有三种：插入字母、删除字母、替换字母。  
首先通过递归的方式来看一下思路。  

```python
class Solution(object):
    # 递归的方法会超时
    def minDistanceByRecursive(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
```

1. 递归结束条件，当传入的`word1`和`word2`有一个为空，最小修改次数就是另一个单词的长度，直接返回即可。

```python
        # 如果word1或word2为空
        if word1 == "":
            return len(word2)
        if word2 == "":
            return len(word1)
```

2. 如果`word1[0] == word2[0]`，递归向下求解。

```python
        # 如果word1[0] == word2[0]
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
```

3. 如果`word1[0] != word2[0]`，分别求出插入、删除、替换的次数，然后选择三个中最小的，返回。

```python
        # 如果 word1[0] != word2[0]
        else:
            # 在word1前插入word2[0]
            insert = 1 + self.minDistance(word1, word2[1:])
            # 删除word1[0]
            delete = 1 + self.minDistance(word1[1:], word2)
            # 用替换word1[0]替换word2[0]
            replace = 1 + self.minDistance(word1[1:], word2[1:])

            return min(insert, delete, replace)
```

当然，简单的递归并不能ac这道题，因为递归的时间复杂度过高(O(3^min(len(word1), len(word2))))，超时了。递归只是更方便我们找到这道题的思路，最后将递归转化为动态规划，保存求解过程中的参数，时间复杂度变为(O(len(word1) * len(word2)))，就ac了。

```python
    # 动态规划做法
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        num1 = len(word1)
        num2 = len(word2)

        memo = [[0] * (num1+1) for i in range(num2+1)]
        
        for i in range(num2, -1, -1):
            for j in range(num1, -1, -1):
                if j == num1:
                    memo[i][j] = num2 - i
                    continue
                if i == num2:
                    memo[i][j] = num1 - j
                    continue
                
                if word1[j] == word2[i]:
                    memo[i][j] = memo[i+1][j+1]
                else:
                    insert = 1 + memo[i][j+1]
                    delete = 1 + memo[i+1][j]
                    replace = 1 + memo[i+1][j+1]
                    memo[i][j] = min(insert, delete, replace)
        return memo[0][0]
```
