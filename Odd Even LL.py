# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        c=head
        f=ListNode()
        e=f
        i=c
        while c and c.next:
            d=ListNode(c.next.val)
            e.next=d
            e=e.next
            c.next=c.next.next
            i=c
            c=c.next
        if not c:
            i.next=f.next
        else:
            c.next=f.next
        return head
        
