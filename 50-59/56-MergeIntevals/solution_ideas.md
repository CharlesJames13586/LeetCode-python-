# 56. Merge Intervals
Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

##### Example 1:
> **Input:** intervals = [[1,3],[2,6],[8,10],[15,18]]  
> **Output:** [[1,6],[8,10],[15,18]]  
> **Explanation:** Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

---
##### 思路：
这道题也比较简单，先把`intervals`按照`start`<sub>`i`</sub>进行升序排列，然后从头扫描`intervals`。
初始化`megerIntervals`为`[intervals[0]]`，然后从第二个（`intervals[1]`）开始扫描，是否可以并入
`megerIntervals[-1]`，能并入就并入，不能并入就直接append()