def solution(citations):
    answer = 0
    temp = sorted(citations)
    #print(temp)
    length = len(temp)
    
    for i in range(temp[length-1]):
        #print("temp", temp[i], "i",i)
        count = 0
        for k in range(length):
            #print("i", i,"k",k, "temp[k]",temp[k])
            if(temp[k] >=i):
                count += 1
                #print(count )
        if(count >= i):
            answer = i
    
    #h번 이상 인용된 논문이 h편이상
    return answer 


#a = [3,0,6,1,5]
#a = [25,8,5,3,3]
#a = [9,7,6,2,1]
a = [0,1,2]
#a = [10,8,5,4,3]
# 0 1 3 5 6
#전체 - i 
print(solution(a))