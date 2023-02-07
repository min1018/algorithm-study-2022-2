import sys
input = sys.stdin.readline
from collections import deque

def solution(numbers, target):
    ans = 0
    q = deque()
    q.append(numbers[0])
    q.append(-numbers[0])
    answer = deque()
    #트리형식으로 쁠마해서 최종 리프노드만 확인 
    
    for i in range(1,len(numbers)):
        while q : 
            temp = q.popleft()
            answer.append(temp)
        while answer:
            temp = answer.popleft()
            q.append(temp + numbers[i])
            q.append(temp - numbers[i])
   
    while q:
        if q.popleft() == target:
            ans += 1
    return ans

