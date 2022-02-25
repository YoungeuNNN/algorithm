heights = [int(input()) for i in range(9)]

for i in range(8):
    if len(heights) != 9:
        break
    for j in range(i+1,9):
        if sum(heights)-heights[i]-heights[j] == 100:
            heights.pop(i)
            heights.pop(j-1)
            break

heights.sort()     
print(*heights,sep='\n')
