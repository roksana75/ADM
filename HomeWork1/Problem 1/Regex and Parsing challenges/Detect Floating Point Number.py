# Detect Floating Point Number
def is_float(number):
    try:
        float(number)
        return '.' in number
    except ValueError:
        return False
queries = int(input())
for _ in range(queries):
    number = input()
    print(is_float(number))