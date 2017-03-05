from sys import stdin, stdout
s = stdin.readline().rstrip()
print 'YES' if '0000000' in s or '1111111' in s else 'NO'
