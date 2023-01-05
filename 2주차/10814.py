import sys
input = sys.stdin.readline

num = int(input())
info = [input().split() for i in range(num)]

temp = sorted(info, key = lambda x:int(x[0]))

for i in range(num):
    print(temp[i][0], temp[i][1])