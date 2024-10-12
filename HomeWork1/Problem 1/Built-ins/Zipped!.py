# Zipped!

n, x = map(int, input().split())
sheet = []
for _ in range(x):
    row = list(map(float, input().split()))
    sheet.append(row)
for column in zip(*sheet):
    average = sum(column) / len(column)
    print(average)
