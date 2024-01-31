# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_st = odd = ListNode()
        even_st = even = ListNode()
        temp = head
        while temp:
            odd.next = temp
            temp = temp.next
            odd = odd.next
            if temp:
                even.next = temp
                temp = temp.next
                even = even.next
                even.next = None
        odd.next = even_st.next
        return head