def approach1(l1,l2): 
    while l2:
        temp = l1
        while temp:
            if temp == l2:
                return l2
            temp = temp.next
        l2 = l2.next
    return None
# Brute Force
# TC = O(m*n)

def approach2(l1,l2):
    st = set()
    while l1:
        st.add(l1)
        l1 = l1.next
    while l2:
        if l2 in st:
            return l2
        l2 = l2.next
    return None
# HAsing
# O(M+N)
        