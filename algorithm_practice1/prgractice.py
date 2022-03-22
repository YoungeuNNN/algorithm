def solution(money, costs):
    arr = [(1, costs[0]), (5, costs[1]), (10, costs[2]),
           (50, costs[3]), (100, costs[4]), (500, costs[5])]
    arr.sort(key=lambda x: (x[0]/x[1]))

    cost = 0
    while money:
        temp = arr[-1][0]
        i = money // temp
        money %=  temp
        cost += i*arr[-1][1]
        arr.pop()
        print(cost)

    answer = 0
    return answer


solution(4578,	[1, 4, 99, 35, 50, 1000])
