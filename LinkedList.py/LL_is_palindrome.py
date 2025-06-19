def palindrome(self,head):
    lst = []
    temp = head
    while temp:
        lst.append(temp.val)
        temp = temp.next
    
    if lst == lst[::-1]:
        return True
    return False