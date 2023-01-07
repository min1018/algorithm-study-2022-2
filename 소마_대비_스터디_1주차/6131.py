import sys
import math
input = sys.stdin.readline

num = int(input())

list = []
for i in range(1,num+1):
    if(num % i == 0):
        list.append(i)

temp = int(len(list)/2)
length = len(list)
count = 0
for i in range(temp):
    if(list[length-1 - i]%2 == 0 and list[i]%2 ==0):
         count = count + 1
    elif(list[length -1 - i]%2 == 1 and list[i]%2==1):
        count = count + 1
print(count)
