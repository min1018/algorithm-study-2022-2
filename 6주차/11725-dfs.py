import sys
imput = sys.stdin.readline
from collections import deque

num = int(input())
graph = [[] for i in range(num+1)]

for _ in range(num-1):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)
    
visited =[0]*(num+1)
arr = []

def dfs(k):
    for i in graph[k]:
        if visited[i] == 0:
            visited[i] = k
            dfs(i)
dfs(1)

for x in range(2, n+1):
    print(visited[x])