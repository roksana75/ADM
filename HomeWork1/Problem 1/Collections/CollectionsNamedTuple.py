# Collections.namedtuple()

from collections import namedtuple
(n, cols) = (int(input()), input().split())
G = namedtuple('G', cols)
marks = [int(G._make(input().split()).MARKS) for _ in range(n)]
print(sum(marks) / len(marks))
