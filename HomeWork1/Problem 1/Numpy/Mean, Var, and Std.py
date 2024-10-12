# Mean, Var, and Std
import numpy as np
N, M = map(int, input().split())
A = np.array([list(map(int, input().split())) for n in range(N)])
print(np.mean(A, axis = 1))
print(np.var(A, axis = 0))
print(np.round(np.std(A), 11))