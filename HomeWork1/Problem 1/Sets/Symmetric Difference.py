# Symmetric Difference
if __name__ == '__main__':
    m = int(input())
    a = set(map(int, input().split()))
    n = int(input())
    b = set(map(int, input().split()))
    
    symmetric_diff = a.symmetric_difference(b)
    
    for elem in sorted(symmetric_diff):
        print(elem)