if __name__ == "__main__":
    setSize = int(raw_input())
    for s in range(setSize):
        arrSizeA = int(raw_input())
        arrA = list(map(int, raw_input().split()))
        arrSizeB = int(raw_input())
        arrB = list(map(int, raw_input().split()))
        arrA.sort()
        arrB.sort()
        
        i = 0
        isSubArr = 0
        while i < arrSizeA:
            j = i
            while j < arrSizeB:
                if arrB[j] == arrA[i]:
                    isSubArr += 1
                    break
                j += 1
            i += 1
                    
        print(isSubArr == arrSizeA)