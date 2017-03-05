from sys import stdin, stdout
n = int(stdin.readline().rstrip())

def solve():
    a, b, c = map(int, stdin.readline().rstrip().split())
    return 1 if a + b + c > 1 else 0

count = 0
for i in range(0, n):
    count += solve()
print count