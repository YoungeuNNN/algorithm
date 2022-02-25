n = int(input())
lst = list(map(int,input().split()))
dp = [-100000000]*n
dp2 = [-100000000]*n
dp[0] = lst[0]
ans = 0
for i in range(1,n):
        dp[i] = max(lst[i],dp[i-1]+lst[i])
        dp2[i] = max(dp[i-1],dp2[i-1]+lst[i])

ans = max(max(dp), max(dp2))
print(ans) 
