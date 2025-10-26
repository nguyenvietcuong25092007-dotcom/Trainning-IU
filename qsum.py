import sys
n, q = map(int, input().split())
a = list(map(int, input().split()))
tmp = [0] * (n + 1)
kq = []

for i in range(n):
    tmp[i + 1] = tmp[i] + a[i]

for i in range(q):
    L, R = map(int, sys.stdin.readline().split())
    tong = tmp[R] - tmp[L-1]
    print(tong)