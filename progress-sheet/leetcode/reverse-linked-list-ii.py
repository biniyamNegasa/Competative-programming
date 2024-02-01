# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1
        start = ListNode(0, head)
        first = start
        while left>count:
            first = first.next
            count+=1
        second = first.next
        while right>count:
            val = second.next
            second.next = val.next
            val.next = first.next
            first.next = val
            count += 1
        return start.next