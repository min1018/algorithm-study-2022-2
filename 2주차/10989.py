import sys
input = sys.stdin.readline

str = input().strip()
ans = []

for i in range(26):
    print(str.find(chr(97+i)),end = ' ')
    
