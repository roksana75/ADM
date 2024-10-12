# Word Order

n = int(input())
line1 = []
for _ in range(n):
    line1.append(input().strip())
result = {}
for str1 in line1:
    result[str1] = result.get(str1, 0) + 1
print(len(result))
print(*result.values())
