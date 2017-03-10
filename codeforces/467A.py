room = 0
for i in range(0, int(raw_input())):
    room += reduce(lambda p,q: p < q-1, map(int, raw_input().rstrip().split()))
print room
