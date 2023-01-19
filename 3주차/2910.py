#완
import sys
input = sys.stdin.readline
from collections import Counter

num, min = map(int,input().split(' '))
temp = Counter(input().strip().split(' ')).most_common()


for i in range(len(temp)):
    for k in range(temp[i][1]):
        print("%d "%int(temp[i][0]) , end='')