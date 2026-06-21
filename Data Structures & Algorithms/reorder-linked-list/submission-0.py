# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head.next or not head.next or not head.next.next:
            return 
        
        slow, fast = head, head.next
        
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        current = slow.next
        slow.next = None
        prev = None
        while(current):
            n = current.next
            current.next = prev
            prev = current
            current = n
        
        first, second = head, prev
        while(second):
            
            t1,t2 = first.next, second.next

            first.next = second
            second.next =t1

            first =t1
            second =t2

        




        