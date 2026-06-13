# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l3 = ListNode()
        carry = 0
        while l1 and l2:
            l3.next = ListNode((l1.val + l2.val + carry) % 10)
            if (l1.val + l2.val + carry) >= 10:
                carry = 1
            else:
                carry = 0
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next

        rest = l1 or l2
        while rest:
            l3.next = ListNode((rest.val + carry) % 10)
            if (rest.val + carry) >= 10:
                carry = 1
            else:
                carry = 0
            rest = rest.next
            l3 = l3.next

        if carry == 1:
            l3.next = ListNode(1)

        return head.next
