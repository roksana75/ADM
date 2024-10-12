# Set .union() Operation

n = int(input())
eng= set( map( int, input().split() ) )
p = int(input())
turkish = set( map( int, input().split() ) )
new_set = eng.union(turkish)
print( len(new_set) )