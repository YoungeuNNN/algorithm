n = int(input())
lst = list(map(int,input().split()))
dpi = [1]*n
dpd = [1]*n
lst2 = lst[::-1]
result = []
for i in range(n):
    for j in range(i):
        if lst[j] < lst[i]:
            dpi[i] = max(dpi[j]+1,dpi[i])

for i in range(n):
    for j in range(i):
        if lst2[j] < lst2[i]:
            dpd[i] = max(dpd[j]+1, dpd[i])


for i in range(n):
    result.append(dpd[i]+dpi[n-i-1]-1)

        
print(max(result))
