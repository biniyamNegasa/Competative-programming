# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        c=head
        if not c:
            return False
        while c.next:
            if c.val == 'u' :
                return True
            else:
                c.val='u'
            c=c.next
        return False
