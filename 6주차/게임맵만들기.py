from collections import deque

def solution(maps):
    answer = 0
    #bfs를 사용하는 이유는 최단 경로를 찾고 싶은 문제니까

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1] 
        
        while q:
            x,y = q.popleft()
            
            for i in range(4):
                nx = dx[i]+x
                ny = dy[i]+y
                
                if len(maps)<= nx or len(maps[0])<= ny or nx<0 or ny<0 : continue #범주 밖
                if maps[nx][ny] == 0: continue #벽
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx,ny))
                    
                    
        return maps[len(maps)-1][len(maps[0]) - 1]
    
    answer = bfs(0,0)

    return -1 if answer == 1 else answer 


