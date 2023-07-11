# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        num1=list1
        num2=list2
        head=ListNode(-101)
        c=head
        while num1 and num2:
            d=ListNode()
            if num1.val<num2.val:
                d.val=num1.val
                c.next=d
                c=c.next
                num1=num1.next
            else:
                d.val=num2.val
                c.next=d
                c=c.next
                num2=num2.next
        while num1:
            d=ListNode()
            d.val=num1.val
            c.next=d
            c=c.next
            num1=num1.next
        while num2:
            d=ListNode()
            d.val=num2.val
            c.next=d
            c=c.next
            num2=num2.next
        return head.next
