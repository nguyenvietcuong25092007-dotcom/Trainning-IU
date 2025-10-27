def tinhtong(n):
    tmp = 0
    if n % 2 == 0:
        for i in range(0, n + 1):
            if i % 2 == 0:
               tmp += 1/i
    else:
        for i in range(0, n + 1):
            if i % 2 != 0:
               tmp += 1/i

    return tmp

n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    tinhtong(a[i])

