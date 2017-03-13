n = int(raw_input())
sumArr = [0, 0, 0]
eq = [0, 0, 0]
for i in range(0, n):
    a = map(int, raw_input().rstrip().split())
    sumArr[0] += a[0]
    sumArr[1] += a[1]
    sumArr[2] += a[2]

print 'YES' if sumArr == eq else 'NO'