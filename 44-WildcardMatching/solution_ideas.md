# 44. Wildcard Matching

Given an input string (`s`) and a pattern (`p`), implement wildcard pattern matching with support for `'?'` and `'*'`
where:

* `'?'` Matches any single character.
* `'*'` Matches any sequence of characters (including the empty sequence).

The matching should cover the **entire** input string (not partial).

##### Example 1:
> **Input:** s = "aa", p = "a"  
> **Output:** false  
> **Explanation:** "a" does not match the entire string "aa".  

___
#####思路
___
使用DFS解决此问题，使用递归的形式可以更加直观的感受解体思路。
递归终止条件（之一）：`s`和`p`字符串为空，返回`True`
```python
    if len(s) == 0 and len(p) == 0:
        return True
```
当`p`不为空时`if len(p) > 0`，有三种情况： 

1. 扫描到`'*'`，这是整个求解树分叉的情况，分别搜索`'*'`匹配长度为0:len(s)的情况，如果匹配成功
   则返回结果，如果不成功，继续向下返回。  
   为了加快扫描速度，当`'*'`后还是`'*'`时，直接跳过前一个`'*'`。
```python
    if p[0] == '*':
        next = 1
        while next < len(p) and p[next] == '*':
            next = next + 1
        for i in range(len(s) + 1):
            if self.isMatch(s[i:], p[next:]):
                return True
            return False
```
2. 扫描到`'?'`时，如果`s`不为空，则`s`和`p`都往前扫描一步，否则，此路匹配失败。
```python
    elif p[0] == '?':
        if len(s) > 0:
            return self.isMatch(s[1:], p[1:])
        elif len(s) == 0:
            return False
```
3. 扫描到其它情况，如果相同，都向前扫描一步，否则，此路匹配失败。
```python
    else:
        if len(s) > 0 and p[0] == s[0]:
            return self.isMatch(s[1:], p[1:])
        else:
            return False
```

如果`p`不为空，此路匹配失败（因为此时`s`肯定不为空，如果`s`也为空，开头就直接会被返回`True`）

___

但是直接使用递归，会出现：当`p`和`s`不匹配时，要搜索所有的路径，如果字符串长度比较长且`p`中`'*'`
比较多时，就会超时，因为这种情况的时间复杂度是指数级的。所以我们要使用非递归形式，并且剪枝掉一些情况。  
初始化两个变量 
```python
star_index = 0      #记录上一个'*'所在的位置
s_start_index = -1  #记录s中与p中（当前扫描的）最后一个'*'匹配后的第一个字符
```
设置扫描条件，`s`中有为扫描的字符
```python
while s_index < s_length:                # s被匹配成功后截止
```
1. 当扫描到`p`的字符是`'?'`时，或扫描到`p`和`s`的字符一样时，继续向后扫描
```python
    # 匹配一个字符的情况
    if p_index < p_lenght and (p[p_index] == '?' or p[p_index] == s[s_index]):
        p_index = p_index + 1
        s_index = s_index + 1
        continue
```
2. 当扫描到`p`的字符是`'*'`时，记录当前位置，默认匹配`s`中的字符长度为0，于是`p`继续向后
   扫描，`s`扫描位置原地不懂，但是需要用`s_start_index`记录一下，当匹配失败时需要用到。 
```python
    # '*'匹配情况
    if p_index < p_lenght and p[p_index] == '*':
        star_index = p_index             # 记录已扫描字符串中最后一个'*'的位置
        p_index = p_index + 1
        s_star_index = s_index           # 默认'*'匹配0个字符
        continue
```
3. 当前面两种情况匹配失败时，可能是`'*'`匹配的字符的长度不对，我们将`'*'`匹配的字符的
   长度加1，将`p`的扫描位置重新放在上一个`'*'`的位置上，将`s_start_index`，加1，并
   将加1后的值赋给`s`的扫描位置记录变量，重新从`'*'`处开始扫描。
```python
    # 如果前两种情况都不成功，试着增加最后一个'*'匹配的字符串的长度
    if s_star_index != -1 and s_star_index < s_length:
        p_index = star_index + 1
        s_star_index = s_star_index + 1
        s_index = s_star_index
        continue
```
4. 如果都失败，匹配失败（s未扫描结束的情况下）

如果`s`扫描结束，查看`p`是否也扫描结束，都结束就是匹配成功，反之失败。当然，要跳过`p`后面
的所有`'*'`字符。
```python
# 扫描p后多余的'*'
while p_index < p_lenght and p[p_index] == '*':
    p_index = p_index + 1
    # 如果p未扫描结束，宣告失败
    return not p_index < p_lenght
```

后者的算法是一种贪心的DFS，因为它使得前面的`'*'`都匹配了尽量少的字符长度（除了最后一个），
由于`'*'`可以匹配任意长度的字符串的性质，才保证了这种算法的正确性。这种算法的时间复杂度是
O(`len(p)`*`len(s)`)。

详细代码请查看代码页[solution_code.py](solution_code.py)。