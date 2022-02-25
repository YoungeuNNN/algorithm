import time
board = []
start = time.time()
for _ in range(5):
    board.append(list(input().rsplit()))
end = time.time()
print(f"{end - start:.5f} sec")
#1.0
board2 = []
start = time.time()
board = [list(input().rsplit()) for _ in range(5)]
end = time.time()
print(f"{end - start:.5f} sec")
#1.9

g = [*range(100)]  # 기억해두기

print(int('234'))

#s = 9999 if a == 0 else a-1 #else if 문 한번에 

print(sum(i.count(0) for i in zone))
#2차원 리스트 zone에서 0의 갯수 한번에세기 
