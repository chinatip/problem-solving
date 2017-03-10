k, n, w = map(int, raw_input().rstrip().split())
sum = 0 
for i in range(1, w+1):
    sum += k*i
print 0 if n - sum > 0 else sum - n