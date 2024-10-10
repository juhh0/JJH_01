#순환
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)



#반복
def fib_2(n):
    if n<= 1:
        return n
    else:
        a = 0
        b = 1
        for i in range(2, n+1):
            a, b = b, a+b
        return b