"""
head = [0,1,2,3]
if empty , then will return none

intution - current head needs to point to previous node, once done move the previous pointer to head and head to next node.
keep on repeating until head is none
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while(head):
            nextNode = head.next
            head.next = prev

            prev = head
            head = nextNode

        return prev
        