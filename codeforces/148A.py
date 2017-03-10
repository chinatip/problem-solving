count = 0
hit = [int(raw_input()), int(raw_input()), int(raw_input()), int(raw_input())]
d = int(raw_input())
for i in range(1, d+1):
    if i % hit[0] == 0 or i % hit[1] == 0 or i % hit[2] == 0 or i % hit[3] == 0:
        count +=1
print count