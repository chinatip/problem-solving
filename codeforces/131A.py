from sys import stdin, stdout

def capLock(s):
    a = ""
    for i in range(0, len(s)):
        a += s[i].lower() if s[i].upper() == s[i] else s[i].upper()
    return a


s = stdin.readline().rstrip()
print capLock(s) if s[1:] == s[1:].upper() or len(s) == 1 else s