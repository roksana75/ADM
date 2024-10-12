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