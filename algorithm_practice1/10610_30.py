#일의 자리수가 0
#각 자리 수를 더했을 때 3으로 나누어 떨어져야 함
n = list(input())
n.sort(reverse=True)
sum=0
for i in n:
    sum+=int(i)
if sum %3!=0 or '0' not in n:
    print(-1)
else:
    print(''.join(n))
