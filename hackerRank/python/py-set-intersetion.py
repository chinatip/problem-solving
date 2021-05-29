if __name__ == "__main__":
    arrSizeA = int(raw_input())
    arrA = set(map(int, raw_input().split()))
    arrSizeB = int(raw_input())
    arrB = set(map(int, raw_input().split()))
    
    AUB = set(arrA | arrB)
    # s.intersection(a)
    print(len(list(AUB)))