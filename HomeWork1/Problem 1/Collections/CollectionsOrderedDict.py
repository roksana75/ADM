# Collections.OrderedDict()

from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    itm, _, qty = input().rpartition(' ')
    d[itm] = d.get(itm, 0) + int(qty)
for itm, qty in d.items():
    print(itm, qty)