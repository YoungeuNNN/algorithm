from sys import stdin
n = int(stdin.readline())
ls = list(map(int,stdin.readline().split()))

dp = [0 for i in range(n)]

for i in range(n):
    for j in range(i):
        if ls[i] > ls[j]:
            dp[i] = max(dp[i],dp[j]+1)

max = max(dp)
print(max+1)
ans = []
for i in range(max,-1,-1):
    if dp[i] == max:
        ans.append(ls[i])

ans.reverse()
print(*ans)



