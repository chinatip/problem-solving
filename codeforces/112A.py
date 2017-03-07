from sys import stdin, stdout
a = stdin.readline().rstrip().lower()
b = stdin.readline().rstrip().lower()
if a > b:
    print 1
elif a == b:
    print 0
else:
    print -1
