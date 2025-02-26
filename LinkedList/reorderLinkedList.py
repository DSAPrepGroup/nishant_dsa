"""
Initiution and steps:
1.Identify the pattern.(first and last elements in samller list gets inserted 1 by 1)
2.Divide the list in two halfs.
3.to Divide we need to find the middle
4.Reverse the second half
5.merge the first and second half.

we need to iterate first half in straight direction and second half in reverse direction.

"""

class Solution:
    def reorderList(self, head: ListNode) -> None:
        # find Middle
        slow,fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half

        second = slow.next
        prev = None
        slow.next = None # as we are splitting 2 parts so end of first part will be null
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2