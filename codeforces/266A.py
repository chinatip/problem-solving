from sys import stdin, stdout

def solve(i):
    s = stdin.readline().rstrip().upper()
    count = 0
    last = s[0]
    for x in range(1, i):
        if s[x] == last:
            count += 1
        last = s[x]
    return count

n = int(stdin.readline().rstrip())
print solve(n)