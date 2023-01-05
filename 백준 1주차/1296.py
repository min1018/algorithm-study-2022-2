import sys
input = sys.stdin.readline

my = input().strip()
print(my)
num = int(input())

temp = [input().strip() for i in range(num)]
    
#print(temp)
standard = ['L','O','V','E']

#for k in range(num):
# ans = [[temp[k].count(standard[i])] for i in range(4)]
  
ans = []
save = []

for k in range(num):
    for i in range(4):
        ans.append(temp[k].count(standard[i]))


        
for k in range(num):
    save = [temp[k].count(standard[i]) for i in range(4)]
    print(k)
    print(save)
    ans.append(save)
    
print(ans)
print("Save")
print(save)
  
#print(ans)