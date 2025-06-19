
class Solution:
    def hasCycle(self, head) -> bool:
        slow = head
        fast = head
        entry = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while slow != entry: #jb tk slow or entry equal nhi hai tb tk True equal hote hi False
                    slow = slow.next
                    entry = entry.next
                return slow
        return None
                
                
        