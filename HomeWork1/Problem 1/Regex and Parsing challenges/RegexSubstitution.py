import re

N = int(input())

for i in range(N):
    a = input()
    a = re.sub(r'(?<=\s)&&(?=\s)', 'and', a)
    a = re.sub(r'(?<=\s)\|\|(?=\s)', 'or', a)
    print(a)
