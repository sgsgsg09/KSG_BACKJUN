from sys import stdin

#new_average
def n_a(arg):
    n = len(arg)
    lis = []
    max_arg = max(arg)
    for i in range(len(arg)):
        lis.append(arg[i] / max_arg * 100)
    print(sum(lis) / n) 
n = int(stdin.readline().strip())
lis = list(map(int, stdin.readline().split()))
n_a(lis)