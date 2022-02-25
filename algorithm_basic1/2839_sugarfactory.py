n = int(input())
result=0
while n>=0:
    if n%5 ==0:#5로 나눈 나머지가 0인 경우
        result += n//5 #5로 나눈 몫 출력
        print(result)
        break
    #5의 배수가 아니라면 3씩 빼주면서 5의 배수인지 판별
    n -=3
    result +=1 #3kg봉지가 추가되는 것

else:
    print('-1')#break로 빠져나가지 못하면 n이 3과 5의 조합이 아니라는 것이다
