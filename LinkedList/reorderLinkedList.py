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
        slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge tow halfs
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2