from sys import stdin

n = int(stdin.readline())

s=""
for i in range(1,n+1):
    s += " "*(n-i) +"*"*i +"\n"

print(s)

#오른쪽을 기준으로 별 찍기.
#별 찍기 2