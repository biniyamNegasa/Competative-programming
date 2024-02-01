# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sl = ListNode()
        start = sl
        temp = head
        while temp:
            dm = sl
            while dm.next and temp.val>=dm.next.val:
                dm = dm.next
            data = temp
            temp = temp.next
            data.next = dm.next
            dm.next = data
        return start.next