t = int(input())
var = []
for i in range(t):
    var.append(int(input()))

dp = [0 for i in range(max(var))]
dp[0],dp[1],dp[2] = 1,2,4

for i in range(3,max(var)):
    dp[i] = (dp[i-1]+dp[i-2]+dp[i-3]) % 1000000009

for i in var:
    print(dp[i-1])
