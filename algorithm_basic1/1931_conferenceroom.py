n = int(input())
conf = []

for _ in range(n):
    start,end = map(int, input().split())
    conf.append((start,end))
    


conf.sort(key = lambda x:(x[1],x[0])) #끝나는 시간빠른 순으로 정렬 같을 때만 시작 시간으로 정렬
#두번째 방법 -> sort 두번인데 끝나는시각으로 한번 소트하고 그걸 늦게 시

end_time =0
count =0
for i in conf:
    if i[0]>= end_time: #시작시간이 저장된 endtime보다 크다면
        end_time = i[1]
        count +=1
print(count)




