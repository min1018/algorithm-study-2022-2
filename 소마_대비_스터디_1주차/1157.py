import sys
input = sys.stdin.readline
from collections import Counter

temp = input().strip().upper()
info = Counter(temp).most_common()

#print(len(info))
if(len(info) == 1):
    print(info[0][0])
else: 
    if(info[0][1] != info[1][1]):
        print(info[0][0])
    
    else:
        print("?")
