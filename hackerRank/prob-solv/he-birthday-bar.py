def birthday(s, d, m):
    count = 0
    loopRange = len(s) - m + 1 if m > 1 else len(s)
    for i in range(loopRange):
        curSum = 0
        for j in range(m):
            curSum += s[i+j]
        if curSum == d:
            count += 1
    return count