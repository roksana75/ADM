# Zeros and Ones
import numpy as np
num = tuple(map(int, input().split()))
print(np.zeros(num, dtype=np.int))
print(np.ones(num, dtype=np.int))