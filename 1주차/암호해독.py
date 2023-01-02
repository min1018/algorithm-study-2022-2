def solution(cipher, code):
    answer = ''
    for i in range(0,len(cipher),1):
        if((i+1) % code == 0):
            answer += cipher[i]
    #k*n-1

    return answer