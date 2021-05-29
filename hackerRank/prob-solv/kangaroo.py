def kangaroo(x1, v1, x2, v2):
    startA = x1
    startB = x2
    for i in range(10000):
        if abs(startB - startA) > 10000:
            return "NO"
        startA += v1
        startB += v2
        if abs(startA - startB) == 0:
            return "YES"
    return "NO"