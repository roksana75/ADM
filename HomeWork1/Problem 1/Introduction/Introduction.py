# Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")

# Python If-Else
n = int(input())
if n % 2 != 0:
    print("Weird")
else:
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")

# Arithmetic Operators
if __name__ == '__main__':
 
    a = int(input())
    b = int(input())
    
    print(a + b)
    
    print(a - b)
    
    print(a * b)

# Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a//b)
    print(a/b)

# Loops
if __name__ == '__main__':
    n = int(input())
for i in range(n):
        print(i * i) 

# Write a function
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
                return False
        else:
            return True 
    else:
        return False

# Print Function
n = int(input())
for i in range(1, n + 1):
    print(i, end='')  