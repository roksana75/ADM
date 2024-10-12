# Set Mutations
m = int(input())
set_a = set(map(int, input().split()))
q = int(input())
for _ in range(q):
    command = input().split()
    set_b = set(map(int, input().split()))
    if command[0] == 'intersection_update':
        set_a.intersection_update(set_b)
    if command[0] == 'update':
        set_a.update(set_b)
    if command[0] == 'symmetric_difference_update':
        set_a.symmetric_difference_update(set_b)
    if command[0] == 'difference_update':
        set_a.difference_update(set_b)
print(sum(set_a))