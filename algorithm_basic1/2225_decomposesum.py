n,k = map(int,input().split())
dp = [[0]*201 for _ in range(201)] #2차원 리스트 한번에 선언

for i in range(201):
    dp[1][i] += 1
    dp[2][i]=i+1

for i in range(2,201):
    dp[i][1]=i
    for j in range(2,201):
        dp[i][j] = (dp[i][j-1]+dp[i-1][j]) % 1000000000

print(dp[k][n])

#dp문제에서 범위가 200 정도로 작다면 모든 경우에 대해 배열 만들기
