n = int(input())
dp = [0]*31
dp[2] = 3
for i in range(4,n+1,2):
    dp[i] = 2 + dp[i-2]*3 + sum(dp[:i-2])*2
    #가로가 n인 타일묶음2개 + 전 거에 2개 붙인거 + 특이한타일묶음 다 붙인거

print(dp[n])

