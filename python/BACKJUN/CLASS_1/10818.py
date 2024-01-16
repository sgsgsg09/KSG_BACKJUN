from sys import stdin

#max, min
def max_min(arg):
    s = ''
    max_value = max(arg)
    min_value = min(arg)
    s += str(min_value) + " " + str(max_value)
    return print(s)

n = int(stdin.readline())

lis = list(map(int, stdin.readline().split()))
max_min(lis)
