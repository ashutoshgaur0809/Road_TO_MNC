# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        lst = []

        temp = head
        while temp:
            lst.append(temp.val)
            temp = temp.next
        
        k = len(lst) - n

        lst.pop(k)
        

        if len(lst) > 0:
            dummy = ListNode(0)
            temp = dummy

            while lst:
                temp.next = ListNode(lst.pop(0))
                temp = temp.next

            return dummy.next
        else:
            return None
        