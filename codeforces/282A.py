from sys import stdin, stdout
n = int(stdin.readline().rstrip())

count = 0
for i in range(0,n):
    s = stdin.readline().rstrip().lower()
    if '++' in s:
        count += 1
    else:
        count -= 1
print count