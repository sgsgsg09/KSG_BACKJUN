from sys import stdin

# n 횟수
def number(arg):
    s = ''
    arg_lis = list(arg[1])
    for t in range(len(arg_lis)):
        for i in range(int(arg[0])):
            s += arg_lis[t]
    return s
# 문자열.
n = int(stdin.readline())
args = []
for i in range(n):
    lis = list(stdin.readline().split())
    args.append(number(lis))

for i in range(n):
    print(args[i])