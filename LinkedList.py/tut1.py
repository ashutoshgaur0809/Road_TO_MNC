class ListNode:
    def __init__(self):
        self.start = None 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
  

def mergeTwoLists(list1, list2):
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        if list1.val > list2.val:
            list1,list2 = list2,list1

        res = list1

        while list1 != None and list2!=None:
            temp = None
            while list1!=None and list1.val <= list2.val:
                temp = list1
                list1 = list1.next
            temp.next = list2
            list1,list2 = list2,list1

        return res

def createLinkedListFromInput():
    values = input("Enter the sorted list values separated by spaces: ").split()
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(int(val))
        current = current.next
    return dummy.next

# Create two sorted linked lists from user input
print("Enter values for the first sorted list:")
l1 = createLinkedListFromInput()
print("Enter values for the second sorted list:")
l2 = createLinkedListFromInput()

# Merge the two sorted linked lists
merged_list = ListNode()
merged_list = mergeTwoLists(l1, l2)

# merged_list.view()

# Display the merged list
print("Merged sorted list:")
current = merged_list
while current is not None:
    print(current.val, end=" -> ")
    current = current.next
print("None")
