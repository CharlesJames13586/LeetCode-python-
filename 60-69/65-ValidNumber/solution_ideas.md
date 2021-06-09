# 65. Valid Number

A **valid number** can be split up into these components (in order):

A **decimal number** or an **integer**.
(Optional) An `'e'` or `'E'`, followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either `'+'` or `'-'`).
One of the following formats:
One or more digits, followed by a dot `'.'`.
One or more digits, followed by a dot `'.'`, followed by one or more digits.
A dot `'.'`, followed by one or more digits.
An integer can be split up into these components (in order):

(Optional) A sign character (either `'+'` or `'-'`).
One or more digits.
For example, all the following are valid numbers: `["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]`, while the following are not valid numbers: `["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]`.

Given a string s, return true if s is a **valid number**.

---
##### 思路：
思路比较简单，全程`if`判断和`while`循环即可。

1. 先将空字符串返回`False`：

```python
        if s == "":
            return False
```

2. 匹配`'+'`和`'-'`:

```python
        # 检查符号'+'和'-'
        if s != "" and s[0] in ['+', '-']:
            s = s[1:]
```

3. 匹配整数位数字：

```python
        # 检查数字
        preDot = False
        preE = False
        while s != "" and s[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            preE = True
            preDot = True
            s = s[1:]
```

4. 匹配小数点`'.'`和小数位数字：

```python
        # 检查小数点和小数位的数
        afterDot = False
        if s != "" and s[0] == '.':
            preE = True
            s = s[1:]
            while s != "" and s[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                afterDot = True
                s = s[1:]
            # 如果存在'.'，但小数点前后都没有数字，则返回False
            if not preDot and not afterDot:
                return False
```

5. 匹配`'e'`或`'E'`和之后的符号和数字：

```python
        # 检查'e'或'E'和之后的数字
        afterE = False
        if preE and s != "" and s[0] in ['e', 'E']:
            s = s[1:]
            # 检查符号'+'和'-'
            if s != "" and s[0] in ['+', '-']:
                s = s[1:]
            while s != "" and s[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                afterE = True
                s = s[1:]
            # 如果有'e'或'E'，但后面没有数字，则不是一个合法的数字
            if afterE == False:
                return False
```

6. 最后如果s为空，则说明参数中的是一个合法数字，否则不是一个合法数字。

```python
        if s == "":
            return True
        else:
            return False
```