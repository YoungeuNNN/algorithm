#1992 #1780 # 2630풀기
import sys
input = sys.stdin.readline
n = int(input())
square = [list(map(int, input().split())) for i in range(n)]
a, b, c = 0, 0, 0


def dac(data, x, y, size):
    first_node = data[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
         	# 다른 데이터가 존재한다면
            if data[i][j] != first_node:
                break
        else:
            continue
        break

    # 단일 데이터 종류로 구성되었다면
    else:
        global a, b, c
        if first_node == -1:
            a += 1
        elif first_node == 0:
            b += 1
        else:
            c += 1
        return
    # 종류에 따라 값을 증가

    # 단일 데이터가 아니기 때문에 분할 정복 실행
    div = size//3
    for i in range(3):
        for j in range(3):
            dac(data, x+i*div, y+j*div, div)


dac(square, 0, 0, n)
print(a, b, c, sep="\n")
