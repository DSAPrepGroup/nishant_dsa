"""
need current pointer for starting consider it as a bookmark used on reading books.
ans pointer to return the head as output.
"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = listNode(0)
        ans = curr

        while(list1 and list2 ):
            if(list1.val > list2.val):
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next

        if(list1):
            curr.next = list1
        if(list2):
            curr.next = list2

        return ans.next
    

