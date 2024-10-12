# Concatenate
import numpy as np
n, m, p = map(int, input().split())
arr_A = np.array([list(map(int, input().split())) for _ in range(n)])
arr_B = np.array([list(map(int, input().split())) for _ in range(m)])
result = np.concatenate((arr_A, arr_B), axis=0)
print(result)