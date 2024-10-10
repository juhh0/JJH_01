import time

count = 0
def hanoi_tower(n, fr, tmp, to):
    global count #gloal 키워드를 사용함으로써 전역변수 count사용
    count += 1
    if(n==1):
        print("원판 1: %s --> %s" %(fr, to))

    else:
        hanoi_tower(n-1, fr, to, tmp)
        print("원판 %d: %s --> %s" %(n, fr, to))
        hanoi_tower(n-1, tmp, fr, to)


n = int(input("높이 입력 :"))

start_time = time.time()
hanoi_tower(n, 'a', 'b', 'c')
end_time = time.time()
print(f"하노이 타워 함수의 총 호출 횟수 :{count}회")


print("실행 시간 :", end_time - start_time)