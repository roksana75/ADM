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