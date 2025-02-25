class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise = head
        rabit = head
        while(rabit and rabit.next):
            tortoise = tortoise.next
            rabit = rabit.next.next

            if(tortoise == rabit):
                return True

        return False