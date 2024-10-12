# Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")

# Python If-Else
# Input from the user
n = int(input())
if n % 2 != 0:  # If n is odd
    print("Weird")
else:  # If n is even
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
    # Check if the year is a leap year
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Year is a leap year
            else:
                return False  # Year is not a leap year
        else:
            return True  # Year is a leap year
    else:
        return False  # Year is not a leap year


# Print Function
n = int(input())
for i in range(1, n + 1):
    print(i, end='')  

# itertools.permutations()
from itertools import permutations 
input_string = input().strip()  
s, k = input_string.split() 
k = int(k) 
sorted_string = sorted(s)
for perm in permutations(sorted_string, k):
    print(''.join(perm))  

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
    # complete this line with a reduce statement
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator

# Power - Mod Power
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    m = int(input())
    
    print(pow(a, b))  # Calculate a raised to the power of b
    print(pow(a, b, m))  # Calculate (a raised to the power of b) modulo m

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

# sWAP cASE
def swap_case(s):
    return s.swapcase()

# String Split and Join
def split_and_join(line):
    words = line.split(" ")
    return "-".join(words)
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# What's Your Name?
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#
def print_full_name(first, last):
    # Write your code here
    print(f"Hello {first} {last}! You just delved into python.")

# Mutations
def mutate_string(string, position, character):
  return string[:position] + character + string[position+1:]

# Find a string
def count_substring(string, sub_string):
    count = 0
    substring_length = len(sub_string)
    for i in range(len(string) - substring_length + 1):
        if string[i:i + substring_length] == sub_string:
            count += 1
            
    return count

# String Validators
if __name__ == '__main__':
    s = input().strip()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))

# Text Alignment
thickness = int(input())  # This must be an odd number
c = 'H'
# Top cone
for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))
# Top pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
# Middle belt
for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))
# Bottom pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
# Bottom cone
for i in range(thickness):
    print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))

# Text Wrap

def wrap(string, max_width):
   return textwrap.fill(string, max_width)

# Designer Door Mat
N, M = map(int, input().strip().split())
for i in range(1, N, 2):
    pattern = ".|." * i
    print(pattern.center(M, '-'))
print("WELCOME".center(M, '-'))
for i in range(N-2, 0, -2):
    pattern = ".|." * i
    print(pattern.center(M, '-'))

# String Formatting
def print_formatted(number):
    width = len(bin(number)[2:])
    
    for i in range(1, number + 1):
        decimal = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexadecimal = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)
        print(f"{decimal} {octal} {hexadecimal} {binary}")

# Alphabet Rangoli
a = "abcdefghijklmnopqrstuvwxyz"
def print_rangoli(size):
    
    no_of_lines = []
    for row in range(size):
        print_ = "-".join(a[row:size])
        no_of_lines.append(print_[::-1] + print_[1:])
    width = len(no_of_lines[0])
    
    for row in range(size-1, 0, -1):
        print(no_of_lines[row].center(width, '-'))
        
    for row in range(size):
        print(no_of_lines[row].center(width, '-'))

# Capitalize!

def solve(s):
    res = s.split(' ')
    res1 = (((i.capitalize() for i in res)))
    return ' '.join(res1)

# The Minion Game
def minion_game(string):
    # your code goes here
    n = len(string)
    comb = ((n)*(n+1))/2
    count_k = 0
    count_s = 0
    count_k = sum([len(string[i:]) for i in range(len(string)) if string[i] in "AEIOU"])
    count_s = comb - count_k
    
    if count_s == count_k:
        print("Draw")
    elif count_s > count_k:
        print("Stuart", int(count_s) )
    else:
        print("Kevin", int(count_k))

# Merge the Tools!
from collections import OrderedDict
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i + k]
        unique_chars = "".join(OrderedDict.fromkeys(substring))
        print(unique_chars)

# Introduction to Sets
def average(array):
    distinct_heights = set(array)
    return round(sum(distinct_heights) / len(distinct_heights), 3)

# Symmetric Difference
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    m = int(input())
    a = set(map(int, input().split()))
    n = int(input())
    b = set(map(int, input().split()))
    
    symmetric_diff = a.symmetric_difference(b)
    
    for elem in sorted(symmetric_diff):
        print(elem)

# No Idea!
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
array = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happiness = 0
for value in array:
    if value in A:
        happiness += 1
    elif value in B:
        happiness -= 1
print(happiness)

# Set .add()
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    country_stamps = set()
    
    for _ in range(n):
        country = input().strip()
        country_stamps.add(country)
    
    print(len(country_stamps))

# Set .discard(), .remove() & .pop()
n = int(input())
s = set(list(map(int, input().split()))[::-1])
N = int(input()) 
for _ in range(N):
    input_data = input().split()
    command = input_data[0]
    if command == 'pop':
        if s:
            s.pop()
    elif command == 'remove':
        s.discard(int(input_data[1]))
    elif command == 'discard':
        s.discard(int(input_data[1]))
print(sum(s))

# Set .union() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
eng= set( map( int, input().split() ) )
p = int(input())
turkish = set( map( int, input().split() ) )
new_set = eng.union(turkish)
print( len(new_set) )

# Set .intersection() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
eng = set( map( int, input().split() ) )
p = int(input())
bangla = set( map( int, input().split() ) )
new_set = eng.intersection(bangla)
print( len(new_set) )

# Set .difference() Operation
n = int(input())
Bangla = set( map( int, input().split() ) )
p = int(input())
turkish = set( map( int, input().split() ) )
new_set = Bangla.difference(turkish)
print( len(new_set))

# Set .symmetric_difference() Operation
n = int(input())
english = set( map( int, input().split() ) )
p = int(input())
franch = set( map( int, input().split() ) )
new_set = english.symmetric_difference(franch)
print( len(new_set) )

# Set Mutations
m = int(input())
set_a = set(map(int, input().split()))
q = int(input())
for _ in range(q):
    command = input().split()
    set_b = set(map(int, input().split()))
    if command[0] == 'intersection_update':
        set_a.intersection_update(set_b)
    if command[0] == 'update':
        set_a.update(set_b)
    if command[0] == 'symmetric_difference_update':
        set_a.symmetric_difference_update(set_b)
    if command[0] == 'difference_update':
        set_a.difference_update(set_b)
print(sum(set_a))

# The Captain's Room
# Enter your code here. Read input from STDIN. Print output to STDOUT
def coptain_room(rooms, k):
    myset = set(rooms)
    result = (sum(myset)*k) - sum(rooms)
    return (result // (k-1))

if __name__ == '__main__':
    k = int( input() )
    rooms = list(map(int, input().split()))
    print(coptain_room(rooms, k))

# Check Subset
tc = int(input())
for _ in range(tc):
    na = int(input())
    sa = set(input().split())
    nb = int(input())
    sb = set(input().split())
    if len(sa.difference(sb)):
        print('False')
    else:
        print('True')

# Check Strict Superset
def is_strict_superset(superset):
    count = int(input())
    for _ in range(count):
        subset = set(input().split())
        if len(subset.difference(superset)):
            return False
    return True
if __name__ == '__main__':
    superset = set(input().split())
    if is_strict_superset(superset):
        print('True')
    else:
        print('False')

# collections.Counter()
from collections import Counter
stock_count = int(input())
stock = Counter(input().split())
order_count = int(input())
revenue = 0
for _ in range(order_count):
    size, cost = input().split()
    if stock[size] > 0:
        revenue += int(cost)
        stock[size] -= 1
print(revenue)

# DefaultDict Tutorial
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m = input().split()
d = defaultdict(list)
for i in range(0, int(n)):
    d[input()].append(i+1)
for i in range(0, int(m)):
    item = input()
    if len(d[item]) == 0:
        print(-1)
    else:
        print(*d[item])
 

# Collections.namedtuple()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
(n, cols) = (int(input()), input().split())
G = namedtuple('G', cols)
marks = [int(G._make(input().split()).MARKS) for _ in range(n)]
print(sum(marks) / len(marks))

# Collections.OrderedDict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    itm, _, qty = input().rpartition(' ')
    d[itm] = d.get(itm, 0) + int(qty)
for itm, qty in d.items():
    print(itm, qty)

# Word Order
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
line1 = []
for _ in range(n):
    line1.append(input().strip())
result = {}
for str1 in line1:
    result[str1] = result.get(str1, 0) + 1
print(len(result))
print(*result.values())

# Collections.deque()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
for _ in range(int(input())):
    args = input().strip().split()
    command = args[0]
    
    if command == 'append':
        d.append(args[1])
    elif command == 'pop':
        if d: 
            d.pop()
    elif command == 'popleft':
        if d:
            d.popleft()
    elif command == 'appendleft':
        d.appendleft(args[1])
print(' '.join(d))

# Piling Up!
from collections import deque
for _ in range(int(input())):
    input()
    q = deque(map(int, input().strip().split()))
    max_v = max(q[0], q[-1])
    ok = True
    while q:
        if len(q) == 1:
            ok = q[0] <= max_v
            break
        if q[0] >= q[-1]:
            nxt = q.popleft()
        else:
            nxt = q.pop()
        if nxt > max_v:
            ok = False
            break
        max_v = nxt
    print("Yes" if ok else "No")

# Company Logo
from collections import Counter

if __name__ == '__main__':
    s = input()
    count_lttr = Counter(sorted(s))
    for c in count_lttr.most_common(3):
        print(*c)

# Calendar Module
# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
from datetime import datetime
print(calendar.day_name[datetime.strptime(input(), '%m %d %Y').weekday()].upper())

# Time Delta
import os
from datetime import datetime
def time_delta(t1, t2):
    time_format = '%a %d %b %Y %H:%M:%S %z'
    delta = abs(datetime.strptime(t1, time_format) - datetime.strptime(t2, time_format))
    return str(int(delta.total_seconds()))
if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        for _ in range(int(input())):
            t1 = input()
            t2 = input()
            fptr.write(time_delta(t1, t2) + '\n')

# Exceptions
# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    try:
        a, b = input().split()
        print(int(int(a) / int(b)))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)

# Incorrect Regex
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for i in range(int(input())):
    try:
        re.compile(input())
        print(True)
    except:
        print(False)

# Zipped!
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x = map(int, input().split())
sheet = []
for _ in range(x):
    row = list(map(float, input().split()))
    sheet.append(row)
for column in zip(*sheet):
    average = sum(column) / len(column)
    print(average)

# Athlete Sort
import sys
if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    matrix = [list(map(int, input().strip().split())) for _ in range(n)]
    k = int(input().strip())
    sorted_matrix = sorted(matrix, key=lambda row: row[k])
    for row in sorted_matrix:
        print(' '.join(map(str, row)))

# ginortS
S = list(input())
S.sort(key=lambda c: (
    c.isdigit() and int(c) % 2 == 0,
    c.isdigit() and int(c) % 2 == 1,
    c.isupper(),
    c.islower(),
    c
))
print(''.join(S))

# Map and Lambda Function
cube = lambda x: x ** 3

def fibonacci(n):
    a, b, c = 0, 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


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

# Re.split()
regex_pattern = r"[.]|,"    # Do not delete 'r'.

# Group(), Groups() & Groupdict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
seq = r'([a-zA-Z0-9])\1+'
match = re.search(seq, input().strip())
print(match.groups()[0] if match else -1)

# Re.findall() & Re.finditer()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

consonants =  '[^aeiou]'
a = re.findall("(?<=" + consonants + ")([aeiou]{2,})" + consonants, input(), re.I)
print('\n'.join(a or ['-1']))

# Re.start() & Re.end()
import re
text = input()
pattern = input()
positions = [(m.start(), m.start() + len(pattern) - 1) for m in re.finditer(f'(?={re.escape(pattern)})', text)]
if positions:
    for pos in positions:
        print(pos)
else:
    print((-1, -1))

# Regex Substitution
import re
N = int(input())
for i in range(N):
    a = input()
    a = re.sub(r'(?<=\s)&&(?=\s)', 'and', a)
    a = re.sub(r'(?<=\s)\|\|(?=\s)', 'or', a)
    print(a)

# Validating Roman Numerals
regex_pattern = r"M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[VX]|V?I{0,3})$"    # Do not delete 'r'.

# Validating phone numbers
import re
n = int(input())
for _ in range(n):
    phone_number = input()
    if re.match(r'[789]\d{9}$', phone_number):
        print('YES')
    else:
        print('NO')

# Validating and Parsing Email Addresses
import re
patrn = r'^<([a-zA-Z][\w\.-]+)@([a-zA-Z]+)\.([a-zA-Z]{1,3})>$'
for _ in range(int(input())):
    name, email = input().split(' ')
    if re.match(patrn, email):
        print(f"{name} {email}")

# Hex Color Code
import re
patrn = r'(?<!^)(#(?:[a-fA-F0-9]{3}|[a-fA-F0-9]{6}))(?=[\s;,)])'
for _ in range(int(input())):
    l = input()
    matches = re.finditer(patrn, l)
    for match in matches:
        print(match.group(1))

# HTML Parser - Part 1
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, t, a):
        print('Start :', t)
        for e in a:
            print('->', e[0], '>', e[1])
    def handle_endtag(self, t):
        print('End   :', t)
    def handle_startendtag(self, t, a):
        print('Empty :', t)
        for e in a:
            print('->', e[0], '>', e[1])
parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())

# HTML Parser - Part 2
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_comment(self, cmt):
        if '\n' in cmt:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        print(cmt)
    def handle_data(self, d):
        if d == '\n': return
        print('>>> Data')
        print(d)
html_content = ""
for _ in range(int(input())):
    html_content += input().rstrip() + '\n'
parser = MyHTMLParser()
parser.feed(html_content)
parser.close()

# Detect HTML Tags, Attributes and Attribute Values
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, t, a):
        print(t)
        [print('-> {} > {}'.format(*attr)) for attr in a]
html_input = '\n'.join([input() for _ in range(int(input()))])
parser = MyHTMLParser()
parser.feed(html_input)
parser.close()

# Validating UID
import re
for _ in range(int(input())):
    s = ''.join(sorted(input()))  # Changed variable name to 's'
    try:
        assert re.search(r'[A-Z]{2}', s)
        assert re.search(r'\d{3}', s)
        assert not re.search(r'[^a-zA-Z0-9]', s)
        assert not re.search(r'(.)\1', s)
        assert len(s) == 10
    except:
        print('Invalid')
    else:
        print('Valid')

# Validating Credit Card Numbers
import re
patrn = re.compile(
    r'^'
    r'(?!.*(\d)(-?\1){3})'
    r'[456]\d{3}'
    r'(?:-?\d{4}){3}'
    r'$')
for _ in range(int(input().strip())):
    print('Valid' if patrn.search(input().strip()) else 'Invalid')

# Validating Postal Codes
regex_integer_in_range = r"^[1-9][\d]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.

# Matrix Script
import re
rows, cols = map(int, input().split())
data = []
for _ in range(rows):
    data.append(input())

result = ''.join(''.join(row) for row in zip(*data))
output = re.sub(r'(?<=\w)([^\w]+)(?=\w)', ' ', result)
print(output)

# XML 1 - Find the Score

def get_attr_number(node):
    return sum([len(node.items()) for node in tree.iter()])

# XML2 - Find the Maximum Depth

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    [depth(element, level) for element in elem.getchildren()]
    maxdepth = level if level > maxdepth else maxdepth
    return maxdepth

# Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        f(['+91 ' + c[-10:-5] + ' ' + c[-5:] for c in l])
    return fun

# Decorators 2 - Name Directory

def person_lister(f):
    def inner(people):
       return map(f, sorted(people, key=lambda x: int(x[2])))
    return inner

# Arrays

def arrays(arr):
    return numpy.array(arr[::-1], float)

# Shape and Reshape
import numpy as np
print(np.array(input().split(), int).reshape(3, 3))

# Transpose and Flatten
import numpy as np
n, m = map(int, input().split())
array = np.array([input().strip().split() for _ in range(n)], int)
print(array.transpose())
print(array.flatten())

# Concatenate
import numpy as np
n, m, p = map(int, input().split())
arr_A = np.array([list(map(int, input().split())) for _ in range(n)])
arr_B = np.array([list(map(int, input().split())) for _ in range(m)])
result = np.concatenate((arr_A, arr_B), axis=0)
print(result)

# Zeros and Ones
import numpy as np
num = tuple(map(int, input().split()))
print(np.zeros(num, dtype=np.int))
print(np.ones(num, dtype=np.int))

# Eye and Identity
import numpy as np
np.set_printoptions(sign=' ')
print(np.eye(*map(int, input().split())))

# Array Mathematics
import numpy as np
n, m = map(int, input().split())
x, y = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
print(x + y, x - y, x * y, x // y, x % y, x ** y, sep='\n')

# Floor, Ceil and Rint
import numpy as np
np.set_printoptions(sign=' ')
a = np.array(input().split(), float)
print(*(i(a) for i in [np.floor, np.ceil, np.rint]), sep='\n')

# Sum and Prod
import numpy as np
m, p = map(int, input().split())
a = np.array([input().split() for _ in range(m)], int)
print(np.prod(np.sum(a, axis=0), axis=0))

# Min and Max
import numpy as np
n, p = map(int, input().split())
a = np.array([input().split() for _ in range(n)], int)
print(np.max(np.min(a, axis=1), axis=0))

# Mean, Var, and Std
import numpy as np
N, M = map(int, input().split())
A = np.array([list(map(int, input().split())) for n in range(N)])
print(np.mean(A, axis = 1))
print(np.var(A, axis = 0))
print(np.round(np.std(A), 11))


# Dot and Cross
import numpy as np
n = int(input())
a = np.array([input().split() for _ in range(n)], int)
b = np.array([input().split() for _ in range(n)], int)
print(np.dot(a, b))

# Inner and Outer
import numpy as np
N = np.array(input().split(), int)
M = np.array(input().split(), int)
print(np.inner(N, M), np.outer(N, M), sep='\n')

# Polynomials
import numpy as np
polyn = [float(x) for x in input().split()]
x = float(input())
print(np.polyval(polyn, x))

# Linear Algebra
import numpy as np
np.set_printoptions(legacy='1.13')
n = int(input())
array = np.array([input().split() for _ in range(n)], float)
print(np.linalg.det(array))

# Birthday Cake Candles
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#
def birthdayCakeCandles(candles):
    big = max(candles)
    return candles.count(big)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    fptr.write(str(result) + '\n')
    fptr.close()

# Number Line Jumps
#!/bin/python3
import math
import os
import random
import re
import sys
def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return "YES" if x1 == x2 else "NO"
    if (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) / (v1 - v2) >= 0:
        return "YES"
    return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])
    result = kangaroo(x1, v1, x2, v2)
    fptr.write(result + '\n')
    fptr.close()

# Viral Advertising
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
def viralAdvertising(n):
    shared = 5
    cumulative = 0
    for _ in range(n):
        liked = shared // 2
        cumulative += liked
        shared = liked * 3
    return cumulative
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    result = viralAdvertising(n)
    fptr.write(str(result) + '\n')
    fptr.close()

# Recursive Digit Sum
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def superDigit(n, k):
    initial_sum = sum(int(digit) for digit in n) * k
    return get_super_digit(initial_sum)
def get_super_digit(p):
    while p >= 10:
        p = sum(int(digit) for digit in str(p))
    return p
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()

# Insertion Sort - Part 1
#!/bin/python3
import math
import os
import random
import re
import sys
def insertionSort1(n, arr):
    last_elmnt = arr[-1]
    i = n - 2
    while i >= 0 and arr[i] > last_elmnt:
        arr[i + 1] = arr[i]
        print(" ".join(map(str, arr)))
        i -= 1
    arr[i + 1] = last_elmnt
    print(" ".join(map(str, arr)))
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)

# Insertion Sort - Part 2
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def insertionSort2(n, arr):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
        
        print(" ".join(map(str, arr)))
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort2(n, arr)

