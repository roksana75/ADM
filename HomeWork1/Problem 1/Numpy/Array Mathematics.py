# Array Mathematics
import numpy as np
n, m = map(int, input().split())
x, y = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
print(x + y, x - y, x * y, x // y, x % y, x ** y, sep='\n')