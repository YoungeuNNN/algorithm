import sys
t = int(input()) #테스트케이스 입력받기

for i in range(t):
    cnt = 1
    ppl=[]
    n=int(input())

    for i in range(n):
        ppl.append(tuple(map(int,sys.stdin.readline().split())))
    
    ppl.sort() #앞에 걸로 오름차순 정렬 된다.,서류를 오름차순으로 정렬했으므로 면접 순위만 비교하면 된다.
    max = ppl[0][1] #이렇게 첫번째 튜플의 첫번째에 접근 가능
    for i in range(1,n): #서류 오름차순 정렬 후이므로 서류1등은 무조건 뽑힘, 따라서 range1부터 시작
        if max>ppl[i][1]: #서류 순위는 낮음, 면접순위는 더 높을 경우(더 좋은 면접 성적 발견!)
            cnt +=1 #지원자는 뽑힘
            max = ppl[i][1] #더 좋은 면접성적이 기준이 된다.
    print(cnt)


