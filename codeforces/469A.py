l = int(raw_input())
x = map(int, raw_input().rstrip().split())[1:]
y = map(int, raw_input().rstrip().split())[1:]


levels = set(range(1,l + 1))
pass_levels = set(x + y)
print "I become the guy." if pass_levels.issuperset(levels) else "Oh, my keyboard!"