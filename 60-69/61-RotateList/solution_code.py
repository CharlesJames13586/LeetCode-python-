# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        
        curNode = head
        preNode = None
        length = 1
        # 找到第k+1个节点
        while length < k+1 and curNode != None:
            preNode = curNode
            curNode = curNode.next
            length += 1
        
        # 如果k比链表的长度大
        if curNode == None:
            length -= 1
            k = k % length
            curNode = head
            for i in range(k):
                preNode = curNode
                curNode = curNode.next
        if k == 0:
            return head
        curNode_1 = head
        preNode_1 = None
        while curNode != None:
            preNode = curNode
            curNode = curNode.next
            preNode_1 = curNode_1
            curNode_1 = curNode_1.next
        preNode.next = head
        preNode_1.next = None

        return curNode_1


if __name__ == "__main__":
    # linked_list = [1, 2, 3, 4, 5]
    # k = 2
    linked_list = [1]
    k = 1
    head = ListNode(linked_list[0], None)
    preNode = head
    for i in range(1, len(linked_list)):
        curNode = ListNode(linked_list[i])
        preNode.next = curNode
        preNode = curNode
    
    solution = Solution()
    result = solution.rotateRight(head, k)
    while result.next != None:
        print(result.val, end=' ')
        result = result.next
    print(result.val)