n = int(raw_input())
n += 1
def isDistinctNumber(n):
    return True if len(set(str(n))) == len(str(n)) else False
    
while not isDistinctNumber(n):
    n += 1
print n