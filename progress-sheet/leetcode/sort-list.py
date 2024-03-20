# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def halves(self, head):
        slow = ListNode(0,head)
        fast = ListNode(0,head)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        left = head
        right = slow.next
        slow.next = None
        return left, right
    def combine(self, head1, head2):
        temp1 = head1
        temp2 = head2
        node = ListNode()
        ans = node
        while temp1 and temp2:
            if temp1.val<=temp2.val:
                node.next = temp1
                temp1 = temp1.next
                node = node.next
            else:
                node.next = temp2
                temp2 = temp2.next
                node = node.next
        while temp1:
            node.next = temp1
            temp1 = temp1.next
            node = node.next
        while temp2:
            node.next = temp2
            temp2 = temp2.next
            node = node.next
        return ans.next
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left, right = self.halves(head)
        l = self.sortList(left)
        r = self.sortList(right)
        return self.combine(l,r)
        