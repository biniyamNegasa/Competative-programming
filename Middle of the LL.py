# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=head
        s=0
        while c:
            s+=1
            c=c.next
        midd=s//2+1
        c=head
        for _ in range(midd-1):
            c=c.next
        return c
