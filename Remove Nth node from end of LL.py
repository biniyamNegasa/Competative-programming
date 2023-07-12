# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c=head
        if not c.next:
            if n==0:
                return head
            else:
                return c.next
        s=0
        while c:
            s+=1
            c=c.next
        c=head
        if n==s:
            c=c.next
            return c
        k=s-n-1
        for _ in range(k):
            c=c.next
        c.next=c.next.next
        return head
