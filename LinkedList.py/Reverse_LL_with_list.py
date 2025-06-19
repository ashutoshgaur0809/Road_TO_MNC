class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        temp = head
        while temp:
            lst.append(temp.val)
            temp = temp.next

        lst = lst[::-1]
        dummy = ListNode(0)
        temp = dummy
        while lst:
            temp.next = ListNode(lst.pop(0))
            temp = temp.next
        
        return dummy.next