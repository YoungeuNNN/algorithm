import sys
input= sys.stdin.readline
n,k=map(int,input().split())
word = []


for _ in range(n):
    word.append(set(input().rstrip()[4:-4]).difference('a','c','i','t','n'))
    #set으로만들어서 중복된 거 없애고 앞뒤 anta,tica 자름, 해당 원소도 미리 차집합으로 빼줌 oh 대박적
    

