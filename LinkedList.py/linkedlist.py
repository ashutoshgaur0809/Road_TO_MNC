class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LL:
    def __init__(self):
        self.start = None
        
    def insertLast(self,value):
        newNode = Node(value)
        if self.start == None:
            self.start = newNode
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
        
    def insertFirst(self,value):
        newNode = Node(value)
        newNode.next = self.start
        self.start = newNode 
         
    def inserti(self,i,value):
        newNode = Node(value)
        temp = self.start
        for i in range(i -1):
            temp = temp.next
        newNode.next = temp.next
        temp.next = newNode
        
    def deli(self,i):
        pre = self.start
        temp = self.start.next
        for i in range(i-1):
            temp = temp.next
            pre = pre.next
        pre.next = temp.next       
                      
    def delFirst(self):
        if self.start == None:
            print("Empty LL")
        else:
            self.start = self.start.next
            
    def delLast(self):
        pre = self.start
        temp = self.start.next
        while temp.next!=None:
            temp = temp.next
            pre = pre.next
        pre.next = None    
                
    def view(self):
        if self.start == None:
            print("Empty LL")
        else:
            temp = self.start
            while temp != None:
                print(temp.data,end=' ')
                temp = temp.next
     
    def lenLL(self):
        if self.start == None:
            print("Empty LL")
        else:
            temp = self.start
            cnt = 0
            while temp!=None:
                temp = temp.next
                cnt = cnt + 1
            print("Len of linkedList is --->",cnt)     
    
    def reverse(self): 
        prev = None
        current = self.start 
        while(current is not None): 
            next = current.next #n c.n
            current.next = prev  #c.n p
            prev = current  #p c
            current = next #c n
        self.start = prev    
        
    def print_middle_element(self):
      slow=self.start
      fast=self.start
      while fast is not None and fast.next is not None:
          slow=slow.next      #slow pointer moves one node
          fast=fast.next.next  #fast pointer moves two nodes
      print("\n\nthe middle element is ",slow.data)   
      
    def middleNode(self):
        n = 0
        temp = self.start
        while temp:
            n += 1
            temp = temp.next
        temp = self.start
        for i in range(n // 2):
            temp = temp.next
        return temp.data 
                         
                
a = LL()
while(True):
    print("Enter Options ==> ")
    print("1.Insert At Start \n2.Insert At last \n3.insert at I index\n")
    print("4.del At Start \n5.del At last \n6.del at I index\n")
    print("7.Len of LL\n8.Reverse\n9.Mid Node\n10.View ")
    ch = int(input())
    if ch == 1:
        a.insertFirst(int(input("Enter Value You want to insert at first-->")))
    elif ch == 2:
         a.insertLast(int(input("Enter Value You want to insert at Last-->")))   
    elif ch == 3:
        a.inserti(int(input("Enter index-->")),int(input("Enter No.-->")))     
    elif ch == 4:
        a.delFirst()
    elif ch == 5:
         a.delLast 
    elif ch == 6:
        a.deli(int(input("Enter index-->")))  
    elif ch == 7:
        a.lenLL()     
    elif ch == 8:
        a.reverse()
        a.view()   
    elif ch == 9:
        a.print_middle_element()
        print("the mid is ->",a.middleNode())
    
        
          
    else:
        a.view()  
          

                                                   