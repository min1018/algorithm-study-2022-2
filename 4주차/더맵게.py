from heapq import heappop, heappush, heapify 

def solution(sco, K):
    num = 0
    sco.sort()
    heapify(sco)
    while True:
        if(sco[0] >= K):
            break
        if(len(sco) == 1):
            num = -1
            break
        heappush(sco, heappop(sco) + (heappop(sco) *2))
        num += 1

    return num

