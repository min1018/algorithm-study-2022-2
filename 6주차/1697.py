import sys
input = sys.stdin.readline
from collections import deque
from itertools import product

def find(a,b):
    q = deque()
    q.append(a)
    visited = [0]*100001

    if a == b:
        print("0")
        return 
    while q:
        k = []
        if visited[b] > 0:
            print(visited[b])
            return 
        temp = q.popleft()
        for j in [temp+1, temp-1, temp*2]:
            if j<100001 and visited[j] == 0 and j>=0:
                visited[j] = visited[temp]+1  
                q.append(j)

a ,b = map(int,input().split(" "))

find(a,b)