from sys import stdin, stdout
n, k = map(int, stdin.readline().rstrip().split())
count = 0
list_a = map(int, stdin.readline().rstrip().split())
max = list_a[k-1]
for x in list_a:
    if x >= max and x > 0:
        count += 1

print count