S = input()
t = 0

for s in S:
    t += 2
    if s == 'A' or s == 'B' or s == 'C':
        t += 1
    elif s == 'D' or s == 'E' or s == 'F':
        t += 2
    elif s == 'G' or s == 'H' or s == 'I':
        t += 3
    elif s == 'J' or s == 'K' or s == 'L':
        t += 4
    elif s == 'M' or s == 'N' or s == 'O':
        t += 5
    elif s == 'P' or s == 'Q' or s == 'R' or s == 'S':
        t += 6
    elif s == 'T' or s == 'U' or s == 'V':
        t += 7
    elif s == 'W' or s == 'X' or s == 'Y' or s == 'Z':
        t += 8

print(t)
