def migratoryBirds(arr):
    arr.sort()
    types = [0] * 6
    mostCount = 0
    freqType = 0
    for val in arr:
        types[val] += 1
        
        if mostCount < types[val]:
            mostCount = types[val]
            freqType = val
        
    return freqType