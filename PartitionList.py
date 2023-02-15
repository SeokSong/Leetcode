# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(-1), ListNode(-1)

        leftPrev, rightPrev = left, right

        while(head):
            if head.val < x:
                leftPrev.next = head
                leftPrev = leftPrev.next
            else:
                rightPrev.next = head
                rightPrev = rightPrev.next
            head = head.next
        
        leftPrev.next = rightPrev.next = None
        leftPrev .next = right.next

        return left.next
