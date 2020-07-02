# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return
        if not head.next:
            return head
        temp = head.val
        head.val = head.next.val
        head.next.val = temp
        self.swapPairs(head.next.next)
        return head
            
        
