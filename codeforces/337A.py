n, m = map(int, raw_input().rstrip().split())
f = sorted(map(int, raw_input().rstrip().split()))
print min(f[i+n-1] - f[i] for i in range(m - n + 1))

