class Stack:
    def __init__(self):
        self.stack = []

    # Push element
    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed to stack")

    # pop method
    def safe_pop(self):
        if len(self.stack) == 0:
            print("Stack is empty! Cannot pop.")
            return None
        else:
            item = self.stack.pop()
            print(f"{item} popped from stack")
            return item

    # Display stack
    def display(self):
        print("Stack:", self.stack)



s = Stack()
s.push(10)
s.push(20)
s.push(30)

s.display()

s.safe_pop()
s.safe_pop()
s.safe_pop()
s.safe_pop()