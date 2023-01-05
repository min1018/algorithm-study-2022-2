import sys
input = sys.stdin.readline

num = int(input())
temp = [input().split() for i in range(num)]
#print(temp)

for i in range(int(num)):
    if(sorted(temp[i][0]) == sorted(temp[i][1])):
        print("%s & %s are anagrams."%(temp[i][0],temp[i][1]))
    else:
        print("%s & %s are Not anagrams."%(temp[i][0], temp[i][1]))
