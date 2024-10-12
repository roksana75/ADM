# Sum and Prod
import numpy as np
m, p = map(int, input().split())
a = np.array([input().split() for _ in range(m)], int)
print(np.prod(np.sum(a, axis=0), axis=0))