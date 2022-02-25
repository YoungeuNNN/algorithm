import datetime
import re

d = dict()
d[1] = 'hi'
d[2] = 'yellow'
print(d)
if 'yellow' in d.values():
    print('yes')
    
print(dir(datetime))

st = 'dsdf'
if 'ㅋ' not in st:
    print('d')
    
paragraph = "Bob hit a ball, the hit BALL"
banned = "hit"

word = re.sub(r'[^\w]',' ',paragraph).lower().split()
print(word)

