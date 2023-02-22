import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
count = 0
q = [0]*1001

q[1] = 1
q[2] = 2

for i in range(3, n+1):
    q[i] = (q[i-1] + q[i-2])%10007
          
print(q[n])
