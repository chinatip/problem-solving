n = 9
m = n * 3

def createMat(n, m):
    for i in range(n):
        halfWidth = m // 2
        halfHeight = n // 2
        line = ''
        if i != halfHeight:
            patternFirstHalf = n - abs(halfHeight - i) * 2
            patternSecondHalf = n - (i - halfHeight) * 2
            patternStep = patternFirstHalf if i < halfHeight else patternSecondHalf
            space = '-' * 3 * abs(i - halfHeight)
            pattern = '.|.' * patternStep
            line = space + pattern + space
        else:
            text = 'welcome'
            extraSpace = m - len(text)
            space = '-' * (extraSpace // 2)
            line = space + text + space
        print(line)

createMat(n,m)