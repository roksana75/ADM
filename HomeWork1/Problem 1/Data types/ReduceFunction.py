# Reduce Function

from functools import reduce
def product(fracs):
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator
