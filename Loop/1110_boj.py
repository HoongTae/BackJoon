n = int(input())
num = n
cnt = 0

while True:
    cnt = cnt + 1
    a = num % 10    # a : 주어진 수의 오른쪽 자리 수
    b = num // 10   # b : 주어진 수의 왼쪽 자리 수
    add = (a + b) % 10
    num = (a * 10) + add
    if num == n:
        break
print(cnt)
