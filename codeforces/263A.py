row = 0
col = 0
for i in range(0, 5):
    a =  map(int, raw_input().rstrip().split())
    if sum(a) != 0:
        col = a.index(1)
        row = i
print abs(col - 2) + abs(row - 2)
        