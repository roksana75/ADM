# Text Wrap

def wrap(string, max_width):
   return textwrap.fill(string, max_width)

N, M = map(int, input().strip().split())
for i in range(1, N, 2):
    pattern = ".|." * i
    print(pattern.center(M, '-'))
print("WELCOME".center(M, '-'))
for i in range(N-2, 0, -2):
    pattern = ".|." * i
    print(pattern.center(M, '-'))