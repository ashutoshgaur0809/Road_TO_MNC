class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sort(self, head, k: int) :
        lst = []
        temp = head
        while temp:
            lst.append(temp.val)
            temp = temp.next
        lst.sort()
        dummy = ListNode(0)
        temp = dummy

        while lst:
            temp.next = ListNode(lst.pop(0))
            temp = temp.next
        return dummy.next