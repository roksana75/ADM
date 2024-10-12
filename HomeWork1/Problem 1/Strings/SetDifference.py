# Set .difference() Operation
n = int(input())
Bangla = set( map( int, input().split() ) )
p = int(input())
turkish = set( map( int, input().split() ) )
new_set = Bangla.difference(turkish)
print( len(new_set))