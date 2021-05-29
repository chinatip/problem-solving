def divisibleSumPairs(n, k, ar):
    count = 0
    i = 0
    for i in range(n-1):
        j = i+1
        while j < n:
            if abs(ar[i] + ar[j]) % k == 0:
                count += 1
            j += 1
        i += 1
    return count
