# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        sz = 0
        temp = head
        while temp:
            sz+=1
            temp = temp.next
        val = sz//k
        nums = [val]*k
        rem = sz%k
        i = 0
        while rem:
            nums[i]+=1
            i+=1
            rem-=1
        ans = []
        temp = head
        i = 0
        while i<k:
            node = temp
            for  _ in range(nums[i]-1):
                temp = temp.next
            if temp:
                t2 = temp.next
                temp.next = None
                temp = t2
            ans.append(node)
            i+=1
        return ans