n,k =map(int,input().split())
value=[]
cnt=0
for _ in range(n):
    value.append(int(input()))


value.sort(reverse=True)

for i in value:
    cnt += k//i
    k = k%i

print(cnt)




