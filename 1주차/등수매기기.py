def solution(score):
    answer = []
    avg = []
    temp = []
    for i in range(len(score)):
        #index라는 함수에서는 알아서 인덱스를 반환해주기 때문에 굳이 저장할 필요가 없다
        #avg.append([i,sum(score[i])/2])
        avg.append(sum(score[i])/2)
    temp = sorted(avg, reverse = True)

    for i in range(len(score)):
        answer.append(temp.index(avg[i])+1)

    return answer
