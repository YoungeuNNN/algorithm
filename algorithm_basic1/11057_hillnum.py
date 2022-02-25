n = int(input())
dp = [[1]*10 for _ in range(n)]

if n>1:
    for i in range(10):
        dp[1][i] = 10-i

for i in range(2,n):
    for j in range(10):
        if j==0:
            dp[i][0] = sum(dp[i-1])
        else:
            dp[i][j] = dp[i][j-1] - dp[i-1][j-1]

print(sum(dp[n-1])%10007)