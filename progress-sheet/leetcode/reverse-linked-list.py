# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = head
        head = head.next
        dummy.next = None
        while head:
            node = head
            head = head.next
            node.next = dummy
            dummy = node
        return dummy