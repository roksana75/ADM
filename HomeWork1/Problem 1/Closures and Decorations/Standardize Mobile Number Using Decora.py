# Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        f(['+91 ' + c[-10:-5] + ' ' + c[-5:] for c in l])
    return fun
