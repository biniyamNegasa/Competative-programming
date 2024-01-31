# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = head
        start = mid
        last = head
        while last and last.next:
            mid = mid.next
            last = last.next.next
        dummy = mid
        mid = mid.next
        dummy.next = None
        while mid:
            node = mid
            mid = mid.next
            node.next = dummy
            dummy = node
        while dummy:
            if start.val!=dummy.val:
                return False
            start = start.next
            dummy = dummy.next
        return True
        