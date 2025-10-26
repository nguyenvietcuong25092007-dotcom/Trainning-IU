n = int(input()) 
a = list(map(int,input().split())) 
b = [] 

for i in range(0, len(a)): 
    for j in range(i + 1, len(a)): 
        if a[i] == a[j]: 
            b.append(abs(i - j)) 
            
if len(b) > 0: 
        print(min(b)) 
else: 
     print('-1')