def solution(num, total):
    answer = []
    mid = int(total/num)
    if (num %2 == 0):
        index = int(num/2) -1
    elif (num %2 == 1):
        index = int(num/2) 
    #index = int(num/2)

    for i in range(num):
        if(i < index):
            answer.append(mid - (index-i))
        elif(i == index):
            answer.append(mid)
        elif(i>index):
            answer.append(mid +(i-index))
            
    return answer

