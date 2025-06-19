class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head, k: int):
        lst = []

        temp = head
        while temp:
            lst.append(temp.val)
            temp = temp.next
        n = len(lst)
        if n == 0:
        # Handle the case where the array is empty
            return
        # handle case where k > n
        k = k % n
       
        lst[:] = lst[-k:] + lst[:-k]
        
        dummy = ListNode(0)
        temp = dummy

        while lst:
            temp.next = ListNode(lst.pop(0))
            temp = temp.next

        return dummy.next