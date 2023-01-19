import sys
input = sys.stdin.readline
from collections import Counter

num = int(input())

info = Counter(input().strip().split())
#print(info)
findnum = int(input())
temp2 = input().strip().split()

for i in range(findnum):
    print("%d "%info[temp2[i]],end ='')
    
    