import sys
input = sys.stdin.readline

n = int(input())
temp = [int(input()) for _ in range(n)]
check = [0 for _ in range(n+1)]


check[0] = temp[0]
check[1] = temp[0]+temp[1]
check[2] = max(temp[0]+temp[2], temp[1]+temp[2])

for i in range(3,n):
    check[i] = max(check[i-3]+temp[i-1]+temp[i], check[i-2]+temp[i])
print(check[n-1])

    
