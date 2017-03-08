n = raw_input()
coins = sorted(map(int, raw_input().split(' ')))[::-1]
useCoin = 0
for i in range(0, len(coins)):
    if sum(coins[:i+1]) > sum(coins[i+1:]):
        useCoin += 1
        break
    else:
        useCoin += 1
print useCoin