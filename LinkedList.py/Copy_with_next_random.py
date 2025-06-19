# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.random = None

def copyRandomList(head):
    if not head:
        return None
    
    temp = head
    # step 1
    while temp:
        new_node = Node(temp.val)
        new_node.next = temp.next
        temp.next = new_node
        temp = temp.next.next
    
    # step 2
    itr = head
    while itr:
        if itr.random:
            itr.next.random = itr.random.next
        itr = itr.next.next
    
    # step 3
    dummy = Node(0)
    itr = head
    temp = dummy
    while itr:
        temp.next = itr.next
        temp = temp.next
        itr.next = temp.next
        itr = itr.next
    
    return dummy.next

def printList(head):
    while head:
        print(f"{head.val}: {head.next.val if head.next else 'NULL'}, {head.random.val if head.random else 'NULL'}")
        head = head.next

if __name__ == "__main__":
    head = None
    
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    
    head = node1
    head.next = node2
    head.next.next = node3
    head.next.next.next = node4
    
    head.random = node4
    head.next.random = node1
    head.next.next.random = None
    head.next.next.next.random = node2
    
    print("Original list: (current node: node pointed by next pointer, node pointed by random pointer)")
    printList(head)
    
    print("\nCopy list: (current node: node pointed by next pointer, node pointed by random pointer)")
    new_head = copyRandomList(head)
    printList(new_head)
