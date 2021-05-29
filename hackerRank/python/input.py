if __name__ == "__main__":
    x, k = map(int, raw_input().split())
    
    total = 0
    for i in range(k):
        total += pow(x, i + 1)
        
    print(True if total == k else False)