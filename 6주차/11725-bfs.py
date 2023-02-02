import sys
imput = sys.stdin.readline
from collections import deque

num = int(input())
graph = [[] for i in range(num+1)]

for _ in range(num-1):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)
    
queue = deque()
queue.append(1)
answer = [0]*(num+1)
#print(graph)

def bfs():
    while queue:
        curr = queue.popleft()
        #print("curr", curr)
        for nxt in graph[curr]:
            if answer[nxt] == 0:
                answer[nxt] = curr
                #print("nxt", nxt)
                #print("answer[nxt]= curr", curr )
                queue.append(nxt)
            
bfs()
res = answer[2:]
for x in res:
    print(x)