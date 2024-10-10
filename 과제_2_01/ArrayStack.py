class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None]*self.capacity
        self.top =-1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity-1

    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = e
        else: pass

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top+1]
        else: pass

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else: pass


stack = ArrayStack(5)  #최대 크기 5인 스택 생성
stack.push(10)
stack.push(20)
stack.push(30)
print("Top element:", stack.peek())
print("Popped element:", stack.pop())
print("Full?:", stack.isFull())
print("Empty?:", stack.isEmpty())