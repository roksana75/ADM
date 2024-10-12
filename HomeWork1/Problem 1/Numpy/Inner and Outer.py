# Inner and Outer
import numpy as np
N = np.array(input().split(), int)
M = np.array(input().split(), int)
print(np.inner(N, M), np.outer(N, M), sep='\n')