# Polynomials
import numpy as np
polyn = [float(x) for x in input().split()]
x = float(input())
print(np.polyval(polyn, x))
