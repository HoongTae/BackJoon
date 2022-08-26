N = int(input())

for n in range(N):
    no = 0
    result = 0
    quiz = input()
    for q in quiz:
        if q == 'X':
            no = 0
        else:
            no += 1
            result += no
    print(result)