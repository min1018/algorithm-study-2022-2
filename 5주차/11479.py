import sys
input = sys.stdin.readline
from collections import deque
from heapq import heappush, heappop, heapify

max = 0
num = int(input())
heap = []
for i in range(num):
    length = int(input())
    temp = list(map(int, input().split(" ")))
    
    for j in range(length):
        heappush(heap, -temp[j])
        
        
    q = deque()
    for k in range(length):
        if(k % 2 == 0):
            q.append(heappop(heap))
        else:
            q.appendleft(heappop(heap))
    max = 0
    print("q" ,q)
    for h in range(length-1):
        if(abs(q[h]-q[h+1]) > max):
            max = abs(q[h]-q[h+1])
    if(q[0]- q[length-1] > max):
        max = abs(q[0]-q[length-1])
    print(max)
        
    

