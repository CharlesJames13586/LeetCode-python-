# 91. Decode Ways
A message containing letters from `A-Z` can be **encode** into numbers using the following mapping:

> 'A' -> "1"  
> 'B' -> "2"  
> ...  
> 'Z' -> "26"  

To **decode** an encoded message, all the digits must be grouped then mapped back into letter using the reverse of the mapping above (there may be mutiple ways). For example, `"11106"` can be mapped into:

* `"AAJF"` with the grouping `(1 1 10 6)`
* `"KJF"` with the grouping `(11 10 6)`

Note that the grouping `(11 1 06)` is invalid becase `"06"` cannot be mapped into `'F'` since `"6"` is different from `"06"`.

Given a string `s` containing only digits, return the **number** of ways to **decode** it.

The test cases are generaed so that the answer fits in a **32-bit** integer.

### **Example 1:**
> Input: s = "12"  
> Output: 2  
> Explanation: "12 could be decoded as "AB" (1 2) or "L" (12).

### **Example 2:**

> Input: s = "226"  
> Output: 3  
> Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

---
### **思路**

递归的分情况讨论即可：
* 首位为0，解析失败，没有这样的字符串
* 首位为1，可以为分为两种：
  * 按照一位数"1"解析
  * 按照两位数"1*"解析
* 首位为2，可以非情况讨论
  * 按照一位数"2"解析
  * 按照两位数"2*"解析，* $\in$ [0-6]
* 首位为[3-9]的其他情况，按照一位数解析

需要注意的是这种自上而下解析的时候，如果遇到"111111"这种，每一步都会分两种情况，时间复杂度是O($2^n$)。为了避免这种情况，我们使用一个备忘录保存每次递归解析的结果，后面每次遇到相同的字符串时，直接从备忘录里将结果拿出来，这样时间复杂度变为O(n)。