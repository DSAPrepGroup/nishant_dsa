
"""
Use the concept of dummy node
Goal is, we will have a gap between left and right pointer which is equal to value of n
So when right pointer reaches end(points to null) our left pointer would be at node which
needs to be removed.
So to remove it from linked list, we will have a dummy node before head of linked list and left pointer will be at dummy node.
Then move right pointer to n places from head. 
Finally, move left and right pointer by one until right reaches end of linked list.
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        #Deletion

        left.next = left.next.next

        return dummy.next