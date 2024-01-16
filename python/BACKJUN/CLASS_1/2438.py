from sys import stdin

n = int(stdin.readline())

s=""
for i in range(1,n+1):
    s += ("*"*i + "\n")
print(s)
