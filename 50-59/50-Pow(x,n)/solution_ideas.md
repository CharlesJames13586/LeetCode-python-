# 50. Pow(x, n)
Implement `pow(x, n)`, which calculates `x` raised to the power `n` (i.e., xn).

##### Example 1:
> **Input:** x = 2.00000, n = 10  
> **Output:** 1024.00000

##### Example 2:
> **Input:** x = 2.10000, n = 3  
> **Output:** 9.26100

##### Example 1:
> **Input:** x = 2.00000, n = -2  
> **Output:** 0.25000  
> **Explanation:** 2^-2^ = 1/2^2^ = 1/4 = 0.25

---
##### 思路：
在写这道题时，我走了一些弯路，虽然最终和答案的复杂度一样，但是过程复杂了一点，其复杂的原因在于，对n的处理。  
```python
        pow1 = self.powWithPositiveExp(x, (n - 1) // 2)
        pow2 = self.powWithPositiveExp(x, n - 1 - (n - 1) // 2)
```
```python
        return x * pow1 * pow2
```
这是我自己的处理方式，无论x是奇数还是偶数，x^n^ = x * x^(n-1)//2^ * x^(n-1) - (n-1)//2^。这样将节点分成了不同的两个分支，
这增加了复杂度，为了弥补这个问题，还需要加入result，使用动态规划的方式将复杂度降为O(logn)。

在提交页面看别人的解法，时间最短的一个解法有：
```python
        if n == 0:
            return 1.0
        elif n == 1:
            return x
        elif n == -1:
            return 1/x

        if n % 2 == 1:
            return x * self.myPow(x, n//2)**2
        else:
            return self.myPow(x, n//2)**2
```
刚开始感觉这个算法缺点什么，在执行完下面两个命令，就大概懂了。
```python
>>>-3//2
-2
>>>-3%2
1
```
这样对负数的处理就是：  
x<sup>-3</sup> = x * x<sup>-2</sup> * x<sup>-2</sup>  
x<sup>-2</sup> = x<sup>-1</sup> * x<sup>-1</sup>  
x<sup>-1</sup> = 1/x  
这个方法只将一个节点分成两个一样的节点，这样就可以只分出一个节点再平方即可，就不是一个二叉树了，复杂度也是O(logn)。