a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort()

if a[0] + a[1] == a[2]:
    print('yes')
else:
    print('no')

if b[0] + b[1] == b[2]:
    print('yes')
else:
    print('no')
