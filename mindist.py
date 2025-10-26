n = int(input())
a = list(map(int, input().split()))
min = 999999999999
tmp = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i] == a[j]:
            if min > abs(j - i):
                  min = abs(j - i)
            tmp += 1
    break

if tmp != 0:
     print(min)
else:
     print('-1')