# collections.Counter()
from collections import Counter
stock_count = int(input())
stock = Counter(input().split())
order_count = int(input())
revenue = 0
for _ in range(order_count):
    size, cost = input().split()
    if stock[size] > 0:
        revenue += int(cost)
        stock[size] -= 1
print(revenue)
