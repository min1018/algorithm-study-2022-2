from collections import deque
from heapq import heappush, heappop, heapify


def solution(people, limit):
    answer = 0
    heap = []
    q = deque()
    for i in range(len(people)):   
        heappush(heap, people[i])
    for i in range(len(people)):
        q.append(heappop(heap))
        
    print(q)
    print(len(q))
    while True:
        if(len(q) == 1):
            answer += 1
            break
        elif(len(q) == 0):
            break
        
        if(q[0]+ (temp:=q.pop()) > limit ):
            print(temp)
            answer += 1
            print("len",len(q))
        else:
            print(q.popleft())
            answer += 1
            print("len",len(q))
        
    return answer

# 50 50 70 80
p = [70, 50, 80, 50]
limit = 100

print(solution(p, limit))