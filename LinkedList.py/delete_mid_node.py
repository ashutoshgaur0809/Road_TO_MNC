class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head):
        lst = []

        temp = head
        while temp:
            lst.append(temp.val)
            temp = temp.next
        # mid index
        k = len(lst) // 2
     

        lst.pop(k)
        

        
        dummy = ListNode(0)
        temp = dummy

        while lst:
            temp.next = ListNode(lst.pop(0))
            temp = temp.next

        return dummy.next
    
# Input: head = [1,3,4,7,1,2,6]
# Output: [1,3,4,1,2,6]
# Input: head = [1,2,3,4]
# Output: [1,2,4]
# Input: head = [2,1]
# Output: [2]