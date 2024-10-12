
# List Comprehensions
if __name__ == '__main__':
    x = int(input()) 
    y = int(input())  
    z = int(input())  
    n = int(input())  
    
    result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]
    
    print(result)

# Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split())) 
    unique_scores = list(set(arr))
    unique_scores.sort(reverse=True)
    runner_up_score = unique_scores[1]
    
    print(runner_up_score)

# Nested Lists
if __name__ == '__main__':
    students = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    scores = sorted(set([student[1] for student in students]))
    
    second_lowest_score = scores[1]
    
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest_score]
    
    second_lowest_students.sort()
    
    for name in second_lowest_students:
        print(name)

# Finding the percentage
if __name__ == '__main__':
    n = int(input())
    
    student_marks = {}
    
    for _ in range(n):
        data = input().split()
        name = data[0]
        marks = list(map(float, data[1:]))
        student_marks[name] = marks
    
    query_name = input()
    
    average_marks = sum(student_marks[query_name]) / len(student_marks[query_name])
    
    print(f"{average_marks:.2f}")

# Reduce Function

from functools import reduce
def product(fracs):
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator

# Power - Mod Power
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    m = int(input())
    
    print(pow(a, b))  
    print(pow(a, b, m)) 
# Lists
if __name__ == '__main__':
    N = int(input())  
    lst = []  
    
    for _ in range(N):
        command = input().split()  
        
        if command[0] == 'insert':
            lst.insert(int(command[1]), int(command[2]))  
        elif command[0] == 'print':
            print(lst)  
        elif command[0] == 'remove':
            lst.remove(int(command[1]))  
        elif command[0] == 'append':
            lst.append(int(command[1]))  
        elif command[0] == 'sort':
            lst.sort()  
        elif command[0] == 'pop':
            lst.pop()  
        elif command[0] == 'reverse':
            lst.reverse()  

# Tuples
if __name__ == '__main__':
    n = int(input())
    integers = tuple(map(int, input().split()))
    print(hash(integers))