import sys
input = sys.stdin.readline

num = int(input())
temp = list(map(int,input().strip().split(" ")))

for i in range(num-1):
    # amx 가 되면 깨지는데?
    #그럼 그건 우째?
    temp[i] = max(temp[i], temp[i]+temp[i-1])
    #끊긴거 표현 완
    
print(max(temp))