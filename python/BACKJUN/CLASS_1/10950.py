from sys import stdin

def sum_s(arg):
    a = (arg[0] + arg[1])
    return a

n = int(stdin.readline().strip())
lis_n = []

for i in range(n):
    lis = list(map(int, stdin.readline().split()))
    lis_n.append(sum_s(lis))

for x in lis_n:
    print(x)