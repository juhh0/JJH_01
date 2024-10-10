import time
from fibonacci import *

for i in range(1, 40):
    start_1 = time.time()
    fib(i)
    end_1 = time.time()

    start_2 = time.time()
    fib_2(i)
    end_2 = time.time()

    print("n = ",i ,"반복 :", end_2 - start_2, "순환 :", end_1 - start_1)