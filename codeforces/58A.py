s = raw_input()
hello = ['h', 'e', 'l', 'l', 'o']
pointer = 0
isHello = False
for i in s:
    if i == hello[pointer]:
        pointer += 1
        if pointer == 5:
            isHello = True
            break

print 'YES' if isHello else 'NO'