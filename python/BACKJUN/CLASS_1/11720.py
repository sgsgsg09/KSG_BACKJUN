from sys import stdin

# sum of n number
def sonn(arg):
    n = sum(arg)
    print(n)


n = int(stdin.readline())
lis = list(map(int,stdin.readline().strip()))
sonn(lis)