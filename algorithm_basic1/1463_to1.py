from sys import stdin

n = int(stdin.readline())
dp = [0]*(n+1)
dp[0] = ''


for i in range(2,n+1):

    dp[i]= dp[i-1] +1 #1을뺐을때도 고려해주는 것

    if i%2 == 0:
        dp[i] = min(dp[i],dp[i//2]+1)
    if i%3 == 0:
        dp[i] = min(dp[i],dp[i//3]+1)



print(dp[n])
