n = int(raw_input())

def check_composite(k):
    for j in range(2, k):
        if k % j == 0 and j != k:
            return True
    return False

for i in range(2, n):
    if check_composite(i) and check_composite(n-i):
        print "%d %d" % (i, n-i)
        break 