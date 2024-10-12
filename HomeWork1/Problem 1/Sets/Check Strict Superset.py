# Check Strict Superset
def is_strict_superset(superset):
    count = int(input())
    for _ in range(count):
        subset = set(input().split())
        if len(subset.difference(superset)):
            return False
    return True
if __name__ == '__main__':
    superset = set(input().split())
    if is_strict_superset(superset):
        print('True')
    else:
        print('False')
