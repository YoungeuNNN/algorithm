
r,c = map(int,input().split())
board = []#문자열을 하나씩 리스트로 만들어줌 
for _ in range(r):
    board.append(list(input()))
maxResult=0
move = [(1,0),(-1,0),(0,1),(0,-1)]
alphabet =set()
alphabet.add(board[0][0])
#idea! alphabet을 셋으로 두면 편하다!
#하나의 아이디어 더! 알파벳을 리스트로 만들면 더 빠르다  
def dfs(x,y,result):
    global maxResult
    
    maxResult = max(result,maxResult)
    
    for dx,dy in move:
        x1 = x+dx
        y1 = y+dy
        if 0<=x1<r and 0<=y1<c and not board[x1][y1] in alphabet:
                alphabet.add(board[x1][y1])
                dfs(x1,y1,result+1)
                alphabet.remove(board[x1][y1])

        
dfs(0,0,1)
print(maxResult)
    
    

