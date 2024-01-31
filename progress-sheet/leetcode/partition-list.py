# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        now = ListNode()
        half = ListNode()
        half_start = half
        start = now
        temp = head
        while temp:
            if temp.val<x:
                now.next = temp
                temp = temp.next
                now.next.next = None
                now = now.next
            else:
                half.next = temp
                temp = temp.next
                half.next.next = None
                half = half.next
        now.next = half_start.next
        return start.next