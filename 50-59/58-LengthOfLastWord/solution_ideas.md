# 58. Length of Last Word

Given a string `s` consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return `0`.

A word is a maximal substring consisting of non-space characters only.

##### **Example 1:**
> **Input:** s = "Hello World"  
> **Output:** 5

##### **Example 2:**
> **Input:** s = " "  
> **Output:** 0

---
##### 思路
比较简单的一道题，直接看代码即可。  
```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_array = s.split(' ')
        while(len(s_array) > 0 and s_array[-1] == ''):
            s_array = s_array[:-1]
        else:
            if len(s_array) == 0:
                return 0
        return len(s_array[-1])
```
直接将字符串用`' '`划分，删掉列表最后的`''`元素，如果列表为空，返回`0`，否则返回列表最后一个元素的长度即可。