N = int(input())
score = list(map(int, input().split()))
M = max(score)

new_score = []

for s in score:
    new_score.append(s / M * 100)

print(sum(new_score)/len(new_score))