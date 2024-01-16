from sys import stdin

#four-calculation
def fo_cal(arg):
    print(arg[0] + arg[1])
    print(arg[0] - arg[1])
    print(arg[0] * arg[1])
    print(arg[0] // arg[1])
    print(arg[0] % arg[1])


lis = list(map(int, stdin.readline().split()))
fo_cal(lis)