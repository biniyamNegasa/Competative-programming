# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        holder=head
        while holder:
            while holder.next and holder.next.val==holder.val:
                holder.next=holder.next.next
            holder=holder.next
        return head
