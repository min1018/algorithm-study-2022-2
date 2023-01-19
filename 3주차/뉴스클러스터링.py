import sys
input = sys.stdin.readline
import math

def solution(str1, str2):
    #인덱싱을 사용해서 쪼갠다음
    str1 = str1.lower()
    str2 = str2.lower()

    temp1 = []
    for i in range(len(str1)-1):
        if(str1[i:i+2].isalpha()):
            temp1.append(str1[i:i+2])

    temp2 = []
    for i in range(len(str2)-1):
        if(str2[i:i+2].isalpha()):
            temp2.append(str2[i:i+2])
   
    resultevery = temp1.copy()
    for_1 = temp1.copy()
    
    for i in temp2:
        if i not in for_1:
            resultevery.append(i)
        else:
            for_1.remove(i)

    #다중 집합을 사용해 합집합 교집합을 계산
    resultand = []
    for i in temp2: #리스트를 포문에 넣으면 알아서 하나씩 나오구나
        if i in temp1:
            temp1.remove(i)
            resultand.append(i)

    if(len(resultevery)==0):
        return 65536
    else:
        return math.trunc(len(resultand)/len(resultevery)*int(65536))
    
    
print(solution("FRANCE", "french"))
print(solution("aa1+aa2","AAAA12"))
print(solution("handshake","shake hands"))
print(solution("E=M*C^2","e=m*c^2"))