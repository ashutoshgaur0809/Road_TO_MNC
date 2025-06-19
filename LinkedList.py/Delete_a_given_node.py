class Node:
    def __init__(self, data= 0):
        self.data = data
        self.next = None

# function to get reference of the node to delete
def getNode(l1: Node, val: int) -> Node:
    while l1 is not None and l1.data != val:
        l1 = l1.next
    return l1 #jis jagah pe l1 == val vo address retun hoga

# delete function as per the question
def deleteNode(t: Node) -> None:
    if t is not None and t.next is not None:
        t.data = t.next.data
        t.next = t.next.next
    else:
        # Handle the case where t or t.next is None
        print("Node not found or cannot delete the last node.")

# printing the list function
def printList(l1: Node) -> None:
    while l1 is not None:
        print(l1.data, end=" -> ")
        l1 = l1.next
    print("None")

def createLinkedListFromInput():
    values = input("Enter the sorted list values separated by spaces: ").split()
    dummy = Node()
    current = dummy
    for val in values:
        current.next = Node(int(val))
        current = current.next
    return dummy.next

if __name__ == "__main__":
    # Creating a linked list from user input
    l1 = createLinkedListFromInput()

    # Printing the given list
    print("Given Linked List:")
    printList(l1)

    # Getting a reference to the node with the specified value for deletion
    val_to_delete = int(input("Enter the value to delete: "))
    node_to_delete = getNode(l1, val_to_delete)
    

    # Deleting the node
    deleteNode(node_to_delete)

    # Printing the list after deletion operation
    print("Linked List after deletion:")
    printList(l1)







