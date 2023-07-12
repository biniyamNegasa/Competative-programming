# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head
        d=ListNode(-501)
        e=d
        cl=head
        cr=head
        for _ in range(left-1):
            f=ListNode(cl.val)
            e.next=f
            e=e.next
            cl=cl.next
        for _ in range(right-1):
            cr=cr.next
        o=None
        while left<=right:
            f=ListNode(cl.val)
            f.next=o
            o=f
            cl=cl.next
            left+=1
        e.next=o
        while e.next:
            e=e.next
        while cr:
            e.next=cr.next
            e=e.next
            cr=cr.next
        return d.next
