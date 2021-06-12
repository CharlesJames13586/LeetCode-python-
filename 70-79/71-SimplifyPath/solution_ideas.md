# 71. Simplify Path

Given a string `path`, which is an **absolute path** (starting with a slash `'/'`) to a file or directory in a Unix-style file system, convert it to the simplified **canonical path**.

In a Unix-style file system, a period `'.'` refers to the current directory, a double period `'..'` refers to the directory up a level, and any multiple consecutive slashes (i.e. `'//'`) are treated as a single slash `'/'`. For this problem, any other format of periods such as `'...'` are treated as file/directory names.

The **canonical path** should have the following format:

The path starts with a single slash `'/'`.
Any two directories are separated by a single slash `'/'`.
The path does not end with a trailing `'/'`.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period `'.'` or double period `'..'`)
Return the simplified **canonical path**.

 

##### Example 1:

> **Input:** path = "/home/"  
> **Output:** "/home"  
> **Explanation:** Note that there is no trailing slash after the last directory name.

##### Example 2:

> **Input:** path = "/../"  
> **Output:** "/"  
> **Explanation:** Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

##### Example 3:

> **Input:** path = "/home//foo/"  
> **Output:** "/home/foo"  
> **Explanation:** In the canonical path, multiple consecutive slashes are replaced > by a single one.

##### Example 4:

> **Input:** path = "/a/./b/../../c/"  
> **Output:** "/c"

---
##### 思路：
使用栈解决这个问题。 

```python
class Solution(object):
    def simplifyPath_1(self, path):
        """
        :type path: str
        :rtype: str
        """
```

1. 先将`path`按照`/`划分成数组，去掉空的元素，并初始化一个栈`stack`；

```python
        dirs = [dir for dir in path.split('/') if dir != ""]

        stack = []
```

2. 遍历`dirs`，当遇到`'.'`时，跳过；遇到`'..'`，如果栈不为空，出栈；如果为其它元素，入栈；

```python
        for dir in dirs:
            if dir == '.':
                continue
            if dir == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(dir)
```

3. 拼接`stack`中的元素，返回。

```python
        result = "/" + '/'.join(stack)

        return result
```