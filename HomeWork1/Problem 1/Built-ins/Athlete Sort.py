# Athlete Sort
import sys
if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    matrix = [list(map(int, input().strip().split())) for _ in range(n)]
    k = int(input().strip())
    sorted_matrix = sorted(matrix, key=lambda row: row[k])
    for row in sorted_matrix:
        print(' '.join(map(str, row)))