class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k: int) :
        lst = []
        temp = head
        while temp:
            lst.append(temp.val)
            temp = temp.next
        res = []
        for i in range(0,len(lst),k):
            t = lst[i:i+k]
            if len(t) == k:
                res = res + t[::-1]
            else:
                res = res + t
        dummy = ListNode(0)
        temp = dummy

        while res:
            temp.next = ListNode(res.pop(0))
            temp = temp.next
        return dummy.next