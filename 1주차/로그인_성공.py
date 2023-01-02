def solution(id_pw, db):
    answer = ''
    result = 0
    for i in range(len(db)):
        if db[i][0] == id_pw[0]:
            if db[i][1]==id_pw[1]:
                answer = "login"
                return answer
            else:
                answer = "wrong pw"
                return answer
            
    answer = "fail"
    return answer