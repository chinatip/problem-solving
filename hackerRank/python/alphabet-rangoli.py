def createPattern(n, pace):
    if n == 1:
        return [chr(97 + pace)]
    return [chr(97 + n - 1 + pace)] + createPattern(n-1, pace) + [chr(97 + n - 1 + pace)]

def print_rangoli(n):
    w = n * 3
    l = n*2 -1
    for i in range(l):
        halfHeight = l // 2
        line = ''

        steps = i + 1 if i <= halfHeight else n - (i - halfHeight)
        patterns = createPattern(steps, n - steps)
        pattern = '-'.join(str(x) for x in patterns)
        space = '-' * 2 * abs(i - halfHeight)
        line = space + pattern + space

        print(line)