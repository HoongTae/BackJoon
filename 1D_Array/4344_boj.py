C = int(input())

for i in range(C):
    no = 0
    case = list(map(int, input().split()))
    average = (sum(case) - case[0]) / case[0]
    for j in range(len(case) - 1):
        if case[j+1] > average:
            no += 1
    print("%.3f%%" % (no / case[0] * 100))
