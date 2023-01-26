from collections import defaultdict
def solution(clothes):
    answer = 0
    dict = defaultdict(int)
    for i in range(len(clothes)):
        dict[clothes[i][1]] = dict[clothes[i][1]]+1
        
    ans = [i+1 for i in list(dict.values())]
    answer = 1
    for i in ans:
        answer = answer* i 
    answer = answer -1
    
    return answer 

