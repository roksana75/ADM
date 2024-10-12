# Matrix Script
import re
rows, cols = map(int, input().split())
data = []
for _ in range(rows):
    data.append(input())

result = ''.join(''.join(row) for row in zip(*data))
output = re.sub(r'(?<=\w)([^\w]+)(?=\w)', ' ', result)
print(output)
