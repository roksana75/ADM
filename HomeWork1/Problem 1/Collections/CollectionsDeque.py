# Collections.deque()

from collections import deque
d = deque()
for _ in range(int(input())):
    args = input().strip().split()
    command = args[0]
    
    if command == 'append':
        d.append(args[1])
    elif command == 'pop':
        if d: 
            d.pop()
    elif command == 'popleft':
        if d:
            d.popleft()
    elif command == 'appendleft':
        d.appendleft(args[1])
print(' '.join(d))