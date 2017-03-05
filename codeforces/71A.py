from sys import stdin, stdout
n = int(stdin.readline().rstrip())

def solve(s):
    if len(s) > 10:
        print s[0] + str(len(s) - 2) + s[len(s)-1]
    else:
        print s 

for i in range(0, n):
    s = stdin.readline().rstrip()
    solve(s)