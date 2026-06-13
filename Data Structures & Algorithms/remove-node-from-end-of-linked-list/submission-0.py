# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current,dele,prevdel = head, None, None
        count =0
        while(current):
            count+=1
            current = current.next
            if(count==n):
                dele = head
                continue
            if(dele):
                prevdel = dele
                dele = dele.next
        if prevdel:
            prevdel.next = dele.next
        if dele == head:
            head = head.next
        return head

        


        