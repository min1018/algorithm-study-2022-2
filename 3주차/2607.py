#왜 안돼1 
import sys
input = sys.stdin.readline
from collections import Counter

num = int(input())
temp = [input().strip() for i in range(num)]

standard = Counter(temp[0])
print(standard)
#같은 구성을 갖는 경우
#1. 길이가 같음 -> 같은 구성을 가짐 (set을 해서 같음 )/ 하나를 바꾸면 됨 차집합 하나
#2. 길이가 다름 -> 한문자를 빼거나 한문자를 더하거나 -> 이건 길이 긴 놈을 기준으로 보면 차집합이 0 이거나 1이면 됨 
# 하지만 set을 쓰면 글자의 순서가 문제임 good dog 가 비슷한 단어로 처리가 됨
# 순서를 고려해야함 
#아니 GOD랑 GOA는 되는거야?

count = 0
for i in range(1,num):
 
    ans = Counter(temp[i]) - Counter(temp[0]) if len(temp[i])-len(temp[0])>0 else Counter(temp[0]) - Counter(temp[i])
    print(ans)
    print(sorted(ans.elements()))
    if(len(sorted(ans.elements()))<= 1):
        count = count +1
    #    if(ans)
print(count) 
