# 66. Plus One

Given a **non-empty** array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

##### Example 1:
> **Input:** digits = [1,2,3]  
> **Output:** [1,2,4]  
> **Explanation:** The array represents the integer 123.

---
##### 思路：
这是一道比较简单的题。思路就是模拟手工计算加法。  

```python
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
```

1. 初始化进位和结果数组:

```python
        carry = 0       # 进位
        result = [0] * len(digits)
```

2. 从最后一位开始计算，如果是最后一位，`result[i]`在`digits[i]`的基础上加1，如果是其他位，直接将`digits[i]`赋值给`result[i]`：

```python
        for i in range(len(digits)-1, -1, -1):
            if i == len(digits) - 1:
                result[i] = digits[i] + 1
            else:
                result[i] = digits[i]
```

3. 加上进位的数值`carry`，并且处理当前结果位和下一位进位：

```python
            result[i] += carry
            if result[i] >= 10:
                carry = result[i] // 10
                result[i] = result[i] % 10
            else:
                carry = 0
```

4. 最后，如果循环结束，进位仍大于零，需要将进位加在结果数组的前面：

```python
        if carry > 0:
            result = [carry] + result
        return result
```