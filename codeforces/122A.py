num = raw_input()
luckyNumbers = [4, 7, 47, 74, 77, 444, 447, 477, 744, 747, 777]
isLucky = reduce(lambda y, z: y or z, map(lambda x: int(num) % x == 0, luckyNumbers))
print 'YES' if isLucky or num.translate(None, '47') == '' else 'NO'
