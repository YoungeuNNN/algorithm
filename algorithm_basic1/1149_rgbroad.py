n = int(input())
rgb = [list(map(int,input().split())) for _ in range(n)]

print(rgb[-1])
for i in range(1,n):#두번째 집부터 계산한다.
    #빨간집을 고르는 경우
    rgb[i][0] = min(rgb[i-1][1],rgb[i-1][2]) + rgb[i][0] #첫번째에서 파랑or초록 중 비용이 더 적은 집을 색칠한 후 두번째 집을 빨간색으로 칠하도록
    rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2]) + rgb[i][1]
    rgb[i][2] = min(rgb[i-1][0], rgb[i-1][1]) + rgb[i][2]

print(min(rgb[n-1]))
    

