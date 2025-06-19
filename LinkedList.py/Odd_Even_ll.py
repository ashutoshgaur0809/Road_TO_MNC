# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head):
        lst = [] #[2 1 3 5 6 4 7]
        odd = []  
        even = []
        temp = head
        while temp:
            lst.append(temp.val)
            temp = temp.next

        for i in range(len(lst)):
            #even index append
            if i % 2 == 0: #[2 3 6 7]
                even.append(lst[i])
        for i in range(len(lst)):
            # odd index append
            if i % 2 != 0:#[1 5 4]
                odd.append(lst[i])

        merge = even + odd #[2 3 6 7 1 5 4]

        dummy = ListNode(0)
        temp = dummy

        while merge:
            temp.next = ListNode(merge.pop(0))
            temp = temp.next

        return dummy.next
    
    
    # Wrong hai