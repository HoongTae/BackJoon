def not_self_num(n):
    self = n
    remainder = n
    while True:
        self += remainder % 10
        remainder //= 10
        if remainder == 0:
            break
    return self


list_no = []
list_nsn = []
for i in range(1, 10001):
    list_no.append(i)
for i in range(1, 10001):
    list_nsn.append(not_self_num(i))
    if not_self_num(i) > 10000:
        list_nsn.remove(not_self_num(i))

list_nsn = sorted(list(set(list_nsn)))

for i in range(len(list_nsn)):
    list_no.remove(list_nsn[i])

for j in range(len(list_no)):
    print(list_no[j])