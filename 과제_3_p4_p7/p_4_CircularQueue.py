class CircularQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.array = [None]*capacity
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else: pass

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else: pass

    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
        else: pass

    def __str__(self):
        if self.front < self.rear:
            return str(self.array[self.front+1:self.rear+1])
        else:
            return str(self.array[self.front+1:self.capacity]+self.array[0:self.rear+1])

if __name__ == "__main__":
    q = CircularQueue(10)

    while (True):

        num = int(input(("어떤 연산을 하시겠습니까? : 1.enqueue, 2.dequeue")))

        if (num == 1):
            e = input("추가 값 입력: ")
            q.enqueue(e)
            print(q)

        elif (num == 2):
            q.dequeue()
            print(q)

        msg = input("그만하시겠습니까? y=그만, n=계속")
        if (msg == 'y'):
            break