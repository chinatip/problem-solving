from sys import stdin, stdout
m, n = map(int, stdin.readline().rstrip().split())

if m * n % 2 == 0:
    print m * n / 2
else:
    print (m * n - 1) / 2