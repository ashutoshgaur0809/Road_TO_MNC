class Solution:
    def removeElements(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lst = []
        temp = head
        while temp:
            lst.append(temp.val)
            temp = temp.next
        
        for i in lst:
            if i == k:
                lst.remove(i)
        
        dummy = ListNode(0)
        temp = dummy
        while lst:
            temp.next = ListNode(lst.pop(0))
            temp = temp.next
        
        return dummy.next