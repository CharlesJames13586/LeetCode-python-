# 76. Minimum Window Substring
Hard

---
Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window substring** of `s` such that every character in `t` (**including duplicates**) is included in the window. If there is no such substring, return the empty string `""`.

The testcases will be generated such that the answer is **unique**.

A **substring** is a contiguous sequence of characters within the string.

##### Example 1:
> **Input:** s = "ADOBECODEBANC", t = "ABC"  
> **Output:** "BANC"  
> **Explanation:** The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

##### Example 2:
> **Input:** s = "a", t = "a"  
> **Output:** "a"  
> **Explanation:** The entire string s is the minimum window.


##### Example 3:
> **Input:** s = "a", t = "aa"  
> **Output:** ""  
> **Explanation:** Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

---
##### 思路：
这道题还是有点难度的，思路就是从左往右搜索，使用双指针的想法，当两个指针之前的字符串包含t中的所有单词时，就是一个符合要求的窗口，判断是否小于之前窗口的长度，更新最小窗口，左侧指针向右行进，直到窗体中的单词不能包含t中的所有单词。右侧指针继续向右移动。

```python
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
```

1. 初始化一些所需的变量

```python
        m = len(s)
        n = len(t)
        
        s_sub = []
        s_pos = []
        for i in range(m):
            if s[i] in t:
                s_sub.append(s[i])
                s_pos.append(i)

        # 给t搞个字典
        t_dict = {}
        t_num = 0            # 用来同步t中未匹配剩余字符的个数
        for key in t:
            if key not in t_dict.keys():
                t_dict[key] = 1
            else:
                t_dict[key] += 1
            t_num += 1
        
        t_num_dup = 0        # 记录多匹配字符的个数
        left = 0             # 记录滑动窗口左侧的位置
        old_left = 0
        minwindow = m + 1
        windowLenght = m + 1
```
以例1为例，s = "ADOBECODEBANC", t = "ABC"。  
s_sub是s的子字符串的list形式，里面仅包含了s中的在t中出现的字符串`s_sub = ['A', 'B', 'C', 'B', 'A', 'C']`,  
s_pos是s_sub各字符在s中对应的位置`s_pos = [0, 3, 5, 9, 10, 12]`。  
t_dict是将t转化成了字典的形式，方便存取`t_dict = {'A': 1, 'B': 1, 'C': 1}`。  
t_num是用来同步t中剩余的未匹配的字符(即在双指针之间的动态滑动窗口中未包含的字符)的个数。比如当窗口为`"A"`时，`t_num = 2`，窗口中还缺'B'和'C'，所以是2。  
t_num_dup是用来记录动态滑动窗口中雨t中字符相同但多余的字符的个数。比如当窗口是`"BCBA"`时，因为t中只有一个'B'，窗口中多了一个'B'，所以`t_num_dup = 1`。

2. 遍历`s_sub`

```python
        # 开始遍历
        for i in range(len(s_sub)):
            if t_dict[s_sub[i]] > 0:
                t_dict[s_sub[i]] -= 1
                t_num -= 1
            elif t_dict[s_sub[i]] <= 0:
                t_dict[s_sub[i]] -= 1
                t_num_dup += 1

            while t_num == 0:     # 说明找齐了，使用wihle循环是因为可能要右移好几个重复的字符串
                windowLenght = s_pos[i] - s_pos[left] + 1
                if windowLenght < minwindow:
                    old_left = left
                    minwindow = windowLenght
                    if minwindow == n:      # 因为只有1个解，所以当找到最少的窗口时，可以跳出循环
                        break
                # 窗口右滑1个字符
                if t_dict[s_sub[left]] == 0:
                    t_dict[s_sub[left]] += 1
                    t_num += 1
                elif t_dict[s_sub[left]] < 0:
                    t_dict[s_sub[left]] += 1
                    t_num_dup -= 1
                
                left += 1    
```

从左向右侧遍历，left相当于左指针，i相当于右指针，中间包含的字符串是滑动的窗口。  
右指针右移，更新对应变量。  
当窗口中的字符串包含t中所有的字符时，`t_num == 0`成立。  
求窗口大小，更新最小窗口，记录对应最小窗口的左指针位置。  
同时右移右指针，直到窗口中缺失t中的某一字符。
然后接着右移左指针。

3. 返回结果

```python
        if minwindow == m + 1:    # 说明没有最小窗口
            return ""
        elif minwindow < m + 1:
            return s[s_pos[old_left]: s_pos[old_left] + minwindow]
```