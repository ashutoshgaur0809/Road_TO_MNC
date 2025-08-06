class list:
    def __init__(self):
        self.items = []
    
    def append(self, item):
        self.items.append(item)
        print(f"{item} appended in list")
    
    def remove(self):
        
        if len(self.items) == 0:
            print("List is empty")
        else:
            print(f"{self.items[-1]} removed from list")
            self.items.pop()
        
    def display(self):
        print("List: ", self.items)
    
    def top(self):
        print(f"Top of stack is {self.items[-1]}")
        

obj = list()
ch = 0
while True:
    print("\n1. Append")
    print("2. Remove")
    print("3. Display")
    print("4. Top of stack")
    print("5. Exit")
    
    ch = int(input("Enter Your Choice: "))
    if ch == 1:
        item = int(input("Enter item to append: "))
        obj.append(item)
    
    elif ch == 2:
        obj.remove()
    
    elif ch == 3:
        obj.display()
    
    elif ch == 4:
        obj.top()
    
    else:
        break    
    