# CircularQueue.py
class CircularQueue :
    def __init__( self, capacity = 10 ) :
        self.capacity = capacity        # 용량(고정)
        self.array = [None] * capacity  # 요소들을 저장할 배열
        self.front = 0                  # 전단의 인덱스
        self.rear = 0                   # 후단의 인덱스

    def isEmpty( self ) :
       return self.front == self.rear

    def isFull( self ) :
       return self.front == (self.rear+1)%self.capacity

    def enqueue( self, item ):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item

    def dequeue( self ):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]

    def peek( self ):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]

    def size( self ) :
       return (self.rear - self.front + self.capacity) % self.capacity

    def __str__(self):
        if self.front < self.rear :
            return str(self.array[self.front+1:self.rear+1])
        elif self.front == self.rear:
            return str("[]")
        else :
            return str(self.array[self.front+1:self.capacity] + \
                       self.array[0:self.rear+1] )


capacity = 10
cq = CircularQueue(capacity)

while True:
    command = input("[메뉴선택] e-enqueue(삽입), d-dequeue(삭제), q-종료=> ")

    if command == 'e':
        item = input(" 삽입할 내용: ")
        cq.enqueue(item)
        print(f"큐 상태: {cq}")

    elif command == 'd':
        removed_item = cq.dequeue()
        if removed_item is not None:
            print(f"제거된 항목: {removed_item}")
        print(f"큐 상태: {cq}")

    elif command == 'q':
        break

if __name__=='__main':
    CircularQueue




