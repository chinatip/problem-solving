n = int(raw_input())
p = map(int, raw_input().rstrip().split())
g = {}
result = ''
for i, k in enumerate(p):
    g[k] = i + 1
for i in xrange(n):
    result += str(g[i+1]) + ' '
print result