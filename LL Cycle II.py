# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        f=head
        s=head
        if not head:
            return
        while f.next and f.next.next:
            s=s.next
            f=f.next.next
            if f==s:
                s2=head
                while s2!=s:
                    s=s.next
                    s2=s2.next
                return s
        return
