def solution(phone_book):
    flag = 0
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)-1):
        if(phone_book[i] == phone_book[i+1][0:len(phone_book[i])]):
            answer = False
            flag = 1
            break
    if(flag == 0):
        answer = True
    return answer