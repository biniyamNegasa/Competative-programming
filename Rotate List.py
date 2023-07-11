# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==0:
            return head
        t=head
        s=1
        while t.next:
            t=t.next
            s+=1
        t.next=head
        k%=s
        i=0
        while i<s-k-1:
            i+=1
            head=head.next
        strt=head.next
        head.next=None
        return strt
