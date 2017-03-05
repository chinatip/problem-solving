from sys import stdin, stdout
w = int(stdin.readline().rstrip())

def solve(w):
    isEven = False
    if w % 2 == 0 and w >= 4:
        isEven = True
    print 'Yes' if isEven else 'No'

solve(w)