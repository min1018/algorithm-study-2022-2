import sys
input = sys.stdin.readline

num = int(input())

temp = [0]*10001

for i in range(num):
    temp[int(input())] += 1

for i in range(10001):
    if(temp[i]>0):
        for k in range(temp[i]):
            print(i)