import sys
input = sys.stdin.readline

a,b = map(int,input().split(' '))

tempA = [input().strip().split(" ") for k in range(a)]
tempB = [input().strip().split(" ") for k in range(a)]

answer = [[0 for i in range(b)] for k in range(a)]

for i in range(a):
    for k in range(b):
        answer[i][k] = int(tempA[i][k])+int(tempB[i][k])
        print( answer[i][k],end = ' ')
    print()
