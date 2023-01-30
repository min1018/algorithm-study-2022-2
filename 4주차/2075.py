from heapq import heappush, heappop
import sys
input = sys.stdin.readline

num = int(input())
heap = []

for i in range(num):
    nums = list(map(int,input().strip().split(" ")))
    for k in range(num):
        if(len(heap) >= num):
            if(heap[0]<nums[k]):
                heappop(heap)
                heappush(heap,int(nums[k]))
        else:
            heappush(heap,int(nums[k]))

print(heap[0])



