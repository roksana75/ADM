# Check Subset
tc = int(input())
for _ in range(tc):
    na = int(input())
    sa = set(input().split())
    nb = int(input())
    sb = set(input().split())
    if len(sa.difference(sb)):
        print('False')
    else:
        print('True')