import sys
input = sys.stdin.readline

num = int(input())

bill = [list(map(int,input().strip().split(" "))) for _ in range(num)]

for i in range(1,num):
    bill[i][0] = min(bill[i-1][1], bill[i-1][2])+ bill[i][0]
    bill[i][1] = min(bill[i-1][0], bill[i-1][2])+ bill[i][1]
    bill[i][2] = min(bill[i-1][0], bill[i-1][1])+ bill[i][2]
           
#print(case) 
print(min(bill[num-1][0],bill[num-1][1],bill[num-1][2]))