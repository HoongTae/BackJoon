# N = int(input())
#
# for i in range(N):
#     R, S = input().split()
#     for s in S:
#         print(s * int(R), end='')
#     print()

N = int(input())

for i in range(N):
    result = ''
    R, S = input().split()
    for s in S:
        result += (s * int(R))
    print(result)
