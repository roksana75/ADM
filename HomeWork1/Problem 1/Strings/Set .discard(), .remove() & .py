# Set .discard(), .remove() & .pop()
n = int(input())
s = set(list(map(int, input().split()))[::-1])
N = int(input()) 
for _ in range(N):
    input_data = input().split()
    command = input_data[0]
    if command == 'pop':
        if s:
            s.pop()
    elif command == 'remove':
        s.discard(int(input_data[1]))
    elif command == 'discard':
        s.discard(int(input_data[1]))
print(sum(s))