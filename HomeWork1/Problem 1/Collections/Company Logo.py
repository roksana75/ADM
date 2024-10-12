# Company Logo
from collections import Counter

if __name__ == '__main__':
    s = input()
    count_lttr = Counter(sorted(s))
    for c in count_lttr.most_common(3):
        print(*c)
