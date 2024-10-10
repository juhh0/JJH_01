import re

class ArrayList:
    #리스트의 데이터 : 생성자에서 정의 및 초기화
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.array = [None]*capacity
        self.size = 0

    #리스트의 연산 : 클래스의 메소드
    def isEmpty(self):
        return self.size == 0               #공백상태는 비교 연산 결과를 바로 반환

    def isFull(self):
        return self.size == self.capacity   #포화상태도 비교 연산 결과를 바로 반환

    def getEntry(self, pos):                 #모든 메소드에서 클래스 멤버는 self를 통해 접근하는 것에 유의
        if 0 <= pos < self.size:
            return self.array[pos]
        else : return None

    def replace(self, pos, line):
        self.array[pos] = line

    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= self.size:
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i-1]
            self.array[pos] = e
            self.size += 1                  #예외 상황들은 처리하지 않음
        else : pass

    def delete(self, pos):
         if not self.isEmpty() and 0 <= pos < self.size:
            e = self.array[pos]
            for i in range(pos, self.size-1):
                self.array[i] = self.array[i+1]
            self.size -= 1
            return e
         else : pass                      #예외 상황들은 처리하지 않음

    def _str_(self):
        return str(self.array[0:self.size])


    def make_dictionary(self, input_string):
        # 특수기호를 제외한 단어를 추출
        words = re.findall(r'\b\w+\b', input_string.lower())

        # 단어의 출현 빈도수를 계산
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        # 결과를 dic.txt 파일에 저장
        with open("dic.txt", "w") as file:
            for word, count in sorted(word_count.items()):
                file.write(f"{word} : {count}\n")

        # 결과 출력
        print("단어 출현 빈도수:")
        for word, count in sorted(word_count.items()):
            print(f"{word} : {count}")