from sys import stdin

def multi_sum(arg):
    n = 1
    for i in arg:
        n *= i
    lis = list(str(n))
    lis_t = {}
    for i_t in range(10):
        lis_t[i_t] = 0
    for i in lis:
        lis_t[int(i)] += 1

    return lis_t


lis = []
for i in range(3):
    lis.append(int(stdin.readline()))
for i in range(len(multi_sum(lis))):
    print(multi_sum(lis)[i])