all_cost = int(input())
num = int(input())
s = 0

for n in range(num):
    a, b = map(int, input().split())
    s = s + (a * b)

if s == all_cost:
    print('Yes')
else:
    print('No')