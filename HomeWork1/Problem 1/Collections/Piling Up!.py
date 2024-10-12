# Piling Up!
from collections import deque
for _ in range(int(input())):
    input()
    q = deque(map(int, input().strip().split()))
    max_v = max(q[0], q[-1])
    ok = True
    while q:
        if len(q) == 1:
            ok = q[0] <= max_v
            break
        if q[0] >= q[-1]:
            nxt = q.popleft()
        else:
            nxt = q.pop()
        if nxt > max_v:
            ok = False
            break
        max_v = nxt
    print("Yes" if ok else "No")