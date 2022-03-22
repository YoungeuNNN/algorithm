n = int(input())
state = list(input())
hope = list(input())

def change_zero(light):
    cnt =1
    light[0] = '0' if light[0] == '1' else '1'
    light[1] = '0' if light[1] == '1' else '1'
    
    for i in range(1,len(light)):
        if light[i-1] == hope[i-1]:
            continue
        else:
            cnt+=1
            light[i-1] = '0' if light[i-1] == '1' else '0'
            light[i] = '0' if light[i] == '1' else '0'
            if i<len(light)-1: 
                light[i+1] = '0' if light[i-1] == '1' else '0'
        if hope == light:
            return cnt
        return 2000002
    
def non_change_zero(light):
    cnt=0
    for i in range(1,len(light)):
        if light[i-1] == hope[i-1]:
            continue
        else:
            cnt+=1
            light[i-1] = '0' if light[i-1] == '1' else '0'
            light[i] = '0' if light[i] == '1' else '0'
            if i<len(light)-1:
                light[i+1] = '0' if light[i-1] == '1' else '0'
    print(light)
    print(hope)
    if hope == light:
        return cnt
    return 1000002

cnt1 = change_zero(state[:])
cnt2 = non_change_zero(state[:])
ans = min(cnt1,cnt2)
print(ans)
if ans == 1000002:
    ans = -1
print(ans)
            
    
            
