n = input().split('-')
sum = 0

for i in n[0].split('+'): #첫번째는 더해줘야함(마이너스가 없으므로)
    sum += int(i)

for i in n[1:]: #두번째부터는 마이너스가 나와서 스플릿 된것이므로 빼줘야함
    for j in i.split('+'):
        sum -= int(j)


print(sum)
