from sys import stdin, stdout
word = stdin.readline().rstrip().lower()
word = word.translate(None, 'aeiouy')

result = ''
for i in word:
    result += '.' + i
print result
