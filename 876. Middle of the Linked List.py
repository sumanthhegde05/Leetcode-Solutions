# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        current = head
        middle = head
        while current is not None:
            if count % 2 != 0:
                middle = middle.next
            count += 1
            current = current.next
        return middle
