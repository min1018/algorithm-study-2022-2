def solution(before, after):
    answer = 1
    for i in range(len(before)):
        if(before.count(before[i],0,len(before)) != after.count(before[i],0,len(after))):
            answer = 0
            break
    return answer