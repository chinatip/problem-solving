from sys import stdin, stdout

def count(group):
    count = [0, 0, 0, 0, 0]
    for x in group:
        if x == 4:
            count[4] += 1
        elif x == 3:
            count[3] += 1
        elif x == 2:
            count[2] += 1
        else:
            count[1] += 1
    return count

def calculateNumberOfCar(count):
    car = 0
    car += count[4]
    count[4] = 0

    car += count[2] // 2
    count[2] %= 2

    if count[3] >= count[1]:
        car += count[3]
        count[3] -= count[1]
        count[1] = 0
    else:
        car += count[3]
        count[1] -= count[3]
        count[3] = 0

    if count[2]:
        car += 1
        count[2] = 0
        if count[1] >= 2:
            count[1] -= 2
        else:
            count[1] = 0

    car += count[1] // 4
    count[1] %= 4
    if count[1] > 0:
        car += 1

    return car

n = int(stdin.readline().rstrip())
group = map(int, stdin.readline().rstrip().split())
count = count(group)
car = calculateNumberOfCar(count)
print car