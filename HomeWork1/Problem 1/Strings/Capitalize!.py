# Capitalize!

def solve(s):
    res = s.split(' ')
    res1 = (((i.capitalize() for i in res)))
    return ' '.join(res1)
