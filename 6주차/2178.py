import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split(" "))

#입력 받는거 공부하기 메모    
mat = [list(map(int, list(input().strip()))) for _ in range(n)]
#print(mat)
#print(len(mat))
#print(len(mat[0]))

def bfs(x,y, matrix):
    q = deque()
    q.append((x,y))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if len(matrix)<= nx or len(matrix[0]) <= ny or nx<0 or ny<0: continue
            if matrix[nx][ny] == 0 : continue
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = matrix[x][y] +1
                q.append((nx,ny))
    return matrix[len(matrix) -1 ][len(matrix[0]) -1 ]

print(answer := bfs(0,0,mat))