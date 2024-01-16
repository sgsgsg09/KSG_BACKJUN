from sys import stdin

#find decimal
def f_d(arg):
    #소수란 1과 자기자신을 제외하고 나누어 떨어지지 않아야한다.
    arg_lis = [[] for _ in arg]
    for i in range(len(arg)):
        for x in range(1, arg[i]+1):
            
            result = arg[i] % x 
            if result == 0:
                arg_lis[i].append(x)
    x_n = 0
    non_arg_lis = list(filter(lambda x: x, arg_lis))
    for x in range(len(non_arg_lis)):
        if len(non_arg_lis[x]) == 2:
           x_n += 1
    print(x_n) 



n = int(stdin.readline().rstrip())
lis = list(map(int, stdin.readline().split()))
f_d(lis)
