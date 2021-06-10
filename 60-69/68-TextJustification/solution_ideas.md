68. Text Justification

Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no **extra** space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

##### Example 1:

> **Input:** words = ["This", "is", "an", "example", "of", "text", "justification."], > maxWidth = 16  
> **Output:**  
> [  
> &nbsp;&nbsp;&nbsp;&nbsp;"This&nbsp;&nbsp;&nbsp;&nbsp;is&nbsp;&nbsp;&nbsp;&nbsp;an",  
> &nbsp;&nbsp;&nbsp;&nbsp;"example&nbsp;&nbsp;of&nbsp;text",  
> &nbsp;&nbsp;&nbsp;&nbsp;"justification.&nbsp;&nbsp;"  
> ]

---
##### 思路：

没有什么特殊的思路，就一个一个处理就行。

```python
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
```

1. 先初始化一些参数：

```python
        line_num = 0                   # 记录当前行word的个数
        line_start_index = 0           # 记录当前行第一个word的索引
        line_characters = 0            # 记录当前行words的字符个数
        result = []                    # 用来保存结果
```

2. 循环处理word直到处理完毕：

```python
        while line_start_index < len(words):
```

3. 寻找每一行最多能容纳的words：

```python
            while line_start_index+line_num < len(words) and len(words[line_start_index+line_num]) + line_characters + line_num < maxWidth:
                line_characters += len(words[line_start_index+line_num])
                line_num += 1
```

4. 给这些words匹配好空格：

```python
            rest_space = maxWidth - line_characters
            line = ""
            for i in range(line_num-1):
                if line_start_index + line_num <= len(words):
                    # last_space = int(math.ceil(rest_space / (line_num - 1 - i)))
                    # leetcode的math.ceil()好像有bug
                    last_space = rest_space // (line_num - 1 - i)
                    if rest_space % (line_num - 1 - i) > 0:
                        last_space += 1
                else:
                    last_space = 1
                line += words[line_start_index+i] + ' '*last_space
                rest_space -= last_space
            line += words[line_start_index + line_num - 1]
            line += (maxWidth - len(line)) * ' '
            result.append(line)
```

**注：** LeetCode的`math.ceil()`存在问题，无法正确向上取整，所以这里手动向上取整了。

5. 更新一些参数，进行下一轮循环：

```python
            line_start_index = line_start_index + line_num
            line_characters = 0
            line_num = 0
```

6. 返回结果：

```python
        return result
```