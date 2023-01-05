temp = input()
ans = temp.upper()

max = max(ans)
print(max)
answer = [i for i,v in enumerate(ans) if v == max]
print(answer)

count = 0
for i in range(len(ans)):
    if len(answer) == ans.count(ans[i]):
        count = count +1
if count> ans.count(max):
    print("?")
else:
    print(max)

