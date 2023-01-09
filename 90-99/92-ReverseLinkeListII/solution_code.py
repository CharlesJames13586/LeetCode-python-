from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # left和right是从1开始数的，不是0
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pre = None
        cur = head                     # 当前遍历到的节点
        # 找到left所在的Node
        for _ in range(1, left):
            pre = cur                  # 当前节点的前一个节点
            cur = cur.next
        leftNode = cur                 # 记录left所在的节点
        leftPreNode = pre              # left的前一个节点
        # 开始反转[left,right]区间内的节点
        for _ in range(left, right+1):
            nxt = cur.next             # 当前节点的下一个节点
            cur.next = pre             # 翻转当前节点与上一个节点之间的箭头: '->' => '<-'
            pre = cur
            cur = nxt                  # 通过提前记录的信息迭代cur指针
        if leftPreNode is not None:    # 翻转区间的前一个节点（去掉为空的情况）
            leftPreNode.next = pre     # 指向翻转区间内的最后一个节点
        leftNode.next = cur            # 翻转区间的第一个节点指向翻转区间的后继节点

        # 如果从第一个开始翻转的，返回翻转区间内的最后一个节点（翻转后为头节点）
        if left == 1:
            return pre
        # 如果不是从头开始翻转的，返回原来的头节点就可以了
        elif left > 1:
            return head

