import sys
input = sys.stdin.readline

num = int(input())
distance = list(map(int, input().split(" ")))
cost = list(map(int, input().split(" ")))

total = cost[0]*distance[0]
dist = 0
min = cost[0]
    
for i in range(1, num-1):
    if(min > cost[i]):
        total = total + dist *min
        min = cost[i]
        dist = distance[i]
        print(total)
    else:
        dist+= distance[i]
        print("dist", dist)
        
    if(i == num -2):
        total = total + dist*min
    

print(total)