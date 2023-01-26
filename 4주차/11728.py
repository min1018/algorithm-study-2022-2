from heapq import heappush, heappop, heapify,heapify
import sys
input = sys.stdin.readline

a,b = map(int,input().strip().split(" "))
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))
print(A+B)
print(A.extend(B))

heapify(ans := list(A+B))

while ans:
    print(heappop(ans),end = " ")


#https://wikidocs.net/4308



