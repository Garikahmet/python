# сможество


import random
import time
a = [random.randint(0, 10 * 6) for _ in range(10 ** 6)]
b = set(a)

start = time.perf_counter()
print(110 in a)
end = time.perf_counter()
start1 = time.perf_counter()
print(110 in b)
end1 = time.perf_counter()
print((end - start) / (end1 - start1))