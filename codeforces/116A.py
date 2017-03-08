from sys import stdin, stdout
inTram = 0
minCapacity = 0

def solve(i):
    a, b = map(int, stdin.readline().rstrip().split())
    inTram -= a
    inTram += b
    if i == 0 or inTram > minCapacity:
        minCapacity = inTram

n = int(stdin.readline().rstrip())
for i in range(0, n):
    a, b = map(int, stdin.readline().rstrip().split())
    inTram -= a
    inTram += b
    if i == 0 or inTram > minCapacity:
        minCapacity = inTram
print minCapacity