names = ['Sheldon','Leonard','Penny','Rajesh','Howard']
n = input() - 1
i = 5
while n >= i:
    n -= i
    i *= 2
print names[n / (i / 5)]