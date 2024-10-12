
# The Captain's Room

def coptain_room(rooms, k):
    myset = set(rooms)
    result = (sum(myset)*k) - sum(rooms)
    return (result // (k-1))

if __name__ == '__main__':
    k = int( input() )
    rooms = list(map(int, input().split()))
    print(coptain_room(rooms, k))