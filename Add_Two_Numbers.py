# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first = ListNode()
        current=first
        carry=0
        result=0
        while l1 != None or l2!=None:
            if l1==None:
                result = l2.val+carry
                l2=l2.next

            elif l2==None:
                result = l1.val+carry
                l1=l1.next
                
            else:  
                result = l1.val + l2.val + carry
                l1=l1.next
                l2=l2.next

            if result>9:
                carry=1
                result = result%10
            else:
                carry=0
            new = ListNode(result)
            current.next=new
            current=current.next

        if carry:
            new = ListNode(1)
            current.next=new
            current=current.next
        return first.next
