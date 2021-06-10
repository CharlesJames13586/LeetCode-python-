# 67. Add Binary

Given two binary strings `a` and `b`, return their sum as a binary string.

##### Example 1:

> **Input:** a = "11", b = "1"  
> **Output:** "100"

##### Example 2:

> **Input:** a = "1010", b = "1011"  
> **Output:** "10101"

---
##### 思路：

这道题也可以用模拟手算法来进行二进制的加法操作。

```python
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
```

1. 先将`a`和`b`进行末位对齐，并且初始化进位`carry`和结果数组`c`：

```python
        length = max(len(a), len(b))
        if len(a) < length:
            a = '0' * (length - len(a)) + a
        if len(b) < length:
            b = '0' * (length - len(b)) + b
        carry = 0
        c = ['0'] * length
```

2. 从末位向前开始计算：

```python
        for i in range(length - 1, -1, -1):
            result = int(a[i]) + int(b[i]) + carry
            if result < 2:
                c[i] = str(result)
                carry = 0
            else:
                c[i] = str(result % 2)
                carry = result // 2
```

3. 处理最后一个进位：

```python
        if carry == 1:
            c = ['1'] + c
```

4. 最后将`c`转换为字符串后返回：

```python
        c = ''.join(c)
        return c
```

**注：** 用列表的原因是因为字符串可以通过索引获取值，但不能通过索引进行赋值，因为字符串是不可变对象。