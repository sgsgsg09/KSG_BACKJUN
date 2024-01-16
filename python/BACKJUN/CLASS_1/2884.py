from sys import stdin

#sleep 45mi
def s_45(arg):
    s_45_lis = arg
    def h():
        if(arg[0] - 1 < 0):
            s_45_lis[0] = arg[0] + 23
        else:
            s_45_lis[0] = arg[0] - 1
    if(arg[1] - 45 < 0):
        s_45_lis[1] = arg[1] + 15
        h()
    else:
        s_45_lis[1] = arg[1] - 45
    print(str(s_45_lis[0]) + " " + str(s_45_lis[1]))
lis = list(map(int, stdin.readline().split()))
s_45(lis)
