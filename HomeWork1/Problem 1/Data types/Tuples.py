# Tuples
if __name__ == '__main__':
    n = int(input())
    integers = tuple(map(int, input().split()))
    print(hash(integers))