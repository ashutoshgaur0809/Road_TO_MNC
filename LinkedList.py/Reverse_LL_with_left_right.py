class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lst = []
        temp = head
        while temp:
            lst.append(temp.val)
            temp = temp.next
        
        new_l = lst[:left-1] + lst[left-1:right][::-1] + lst[right:]

        dummy = ListNode(0)
        temp = dummy
        for val in new_l:
            temp.next = ListNode(val)
            temp = temp.next
        
        return dummy.next
    
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [5], left = 1, right = 1
# Output: [5]