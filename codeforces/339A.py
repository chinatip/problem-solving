from sys import stdin, stdout
a = stdin.readline().rstrip().lower()

if len(a) < 2:
    print a

else:
    nums = [ int(a[x]) for x in range(0, len(a), 2)]
    nums = sorted(nums)
    str_a = ''
    for i, y in enumerate(nums):
        if i == len(nums) -1:
            str_a += str(y)
        else:
            str_a += str(y) + "+"
    print str_a