S = input()
alpha = list(range(97, 123))

for i in alpha:
    print(S.find(chr(i)), end=' ')
    