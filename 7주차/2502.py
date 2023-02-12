import sys
input = sys.stdin.readline

nights,ricecake = map(int,input().strip().split(" "))

mem = ["k" for _ in range(nights)]

mem[0] = "a"
mem[1] = "b"
mem[2] = "ab"

for i in range(3,nights):
    mem[i] = mem[i-1]+mem[i-2]
    
d1 = int(mem[nights-1].count("a"))
d2 = int(mem[nights-1].count("b"))

for i in range(1,ricecake):
    if (ricecake - (d2*i))%d1 == 0:
        if (for_d1 := (ricecake- d2*i)/d1) < i:
            print(int(for_d1))
            print(i)
            break 