# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        sizeA = 0
        sizeB = 0
        temp = headA
        while temp:
            sizeA+=1
            temp=temp.next
        temp = headB
        while temp:
            sizeB+=1
            temp=temp.next
        startA = headA
        startB = headB
        val = sizeA-sizeB
        while val>0:
            startA=startA.next
            val-=1
        val = sizeB-sizeA
        while val>0:
            startB=startB.next
            val-=1
        while startA:
            if startA==startB:
                return startA
            startA = startA.next
            startB = startB.next
        return startA