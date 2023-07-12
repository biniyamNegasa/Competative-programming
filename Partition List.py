# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        d=ListNode(-101)
        g=ListNode(0)
        o=g
        e=d
        c=head
        while c:
            if c.val<x:
                e.next=c
                e=e.next
            else:
                y=ListNode(c.val)
                o.next=y
                o=o.next
            c=c.next
        e.next=g.next
        return d.next
