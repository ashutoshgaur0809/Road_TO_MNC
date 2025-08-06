class StackUsingTwoQueues:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, a):
        # q1 ke saare elements q2 mein daalo
        while self.q1:
            self.q2.append(self.q1.pop(0))
        # naya element q1 mein daalo
        self.q1.append(a)
        # q2 ke elements wapas q1 mein daalo
        while self.q2:
            self.q1.append(self.q2.pop(0))
        print("Added element:", a)

    def pop(self):
        # underflow check
        if not self.q1:
            print("Underflow condition: Stack is empty")
            return None
        removed = self.q1.pop(0)
        print("Deleted element is:", removed)
        return removed

    def top(self):
        if not self.q1:
            print("Empty Stack")
            return None
        print("Top of Stack:", self.q1[0])
        return self.q1[0]

    def display(self):
        print("Stack elements :", self.q1)


s = StackUsingTwoQueues()
s.push(100)
s.push(200)
s.push(300)
s.pop()
s.top()
s.display()
