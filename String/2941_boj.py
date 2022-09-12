S = list(input())
cnt = 0

for i in range(len(S)):
    if i == (len(S)-1):
        cnt += 1
    else:
        if S[i] == 'c' or S[i] == 's' or S[i] == 'z':
            if S[i + 1] == '=' or S[i + 1] == '-':
                continue
        elif S[i] == 'd':
            if i + 2 > (len(S)-1):
                cnt += 1
                continue
            elif S[i + 1] == 'z' and S[i + 2] == '=':
                continue
            elif S[i + 1] == '-':
                continue
        elif S[i] == 'l' or S[i] == 'n':
            if S[i + 1] == 'j':
                continue
        cnt += 1

print(cnt)


# ddz=z=jdz
