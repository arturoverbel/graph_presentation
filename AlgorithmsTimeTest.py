from time import time
import numpy as np

PQ = list(range(500000))
t = time()
y, PQ = PQ[-1], PQ[:-1]
time_seconds = time() - t
print(time_seconds)


t = time()
y = PQ.pop(-1)
time_seconds = time() - t
print(time_seconds)
