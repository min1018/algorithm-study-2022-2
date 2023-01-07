import sys
input = sys.stdin.readline

num = int(input())
list = [input().strip() for i in range(num)]

length = len(list[0])

ans = [0]*length

for i in range(num-1):
    for k in range(length):
        if(list[i][k] != list[i+1][k]):
            ans[k] = 1
 
str = ""            
for i in range(length):
    if(ans[i] == 0):
        str = str+list[0][i]
        #print("%c"%list[0][i],end = ' ')
    else:
        str=str+"?"
        #print("?",end = ' ')
print(str)