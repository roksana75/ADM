# Floor, Ceil and Rint
import numpy as np
np.set_printoptions(sign=' ')
a = np.array(input().split(), float)
print(*(i(a) for i in [np.floor, np.ceil, np.rint]), sep='\n')