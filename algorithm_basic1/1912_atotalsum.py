from sys import stdin

n = int(stdin.readline())
ls = list(map(int,stdin.readline().split()))
dp = [0] * n
dp[0] = ls[0]
for i in range(1,n):
    dp[i] = max(ls[i],dp[i-1]+ls[i])

print(max(dp))