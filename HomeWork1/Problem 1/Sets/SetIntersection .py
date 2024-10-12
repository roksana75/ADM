# Set .intersection() Operation

n = int(input())
eng = set( map( int, input().split() ) )
p = int(input())
bangla = set( map( int, input().split() ) )
new_set = eng.intersection(bangla)
print( len(new_set) )