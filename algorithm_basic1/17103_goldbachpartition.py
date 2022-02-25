from sys import stdin
#각 테스트케이스가 가지는 골드바흐 파티션의 갯수 출력하기 출력 : 한 줄에 하나씩
n = int(stdin.readline())
max = 1000000
num = [int(input()) for _ in range(n)]

isprime = [True]*max
isprime[0],isprime[1] = False,False

for i in range(2, int((max)**0.5)+1):  # 에라토스테네스 체 만들기
    if isprime[i]:
        for j in range(i*2, max, i):
            isprime[j] = False



for n in num:
    count = 0
    for i in range((n//2)+1):
        if isprime[i] and isprime[n-i]:
            count+=1
    print(count)