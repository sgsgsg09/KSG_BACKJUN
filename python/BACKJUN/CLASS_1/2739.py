from sys import stdin

#gugudan
def gugu(n:int):
    for i in range(1,10):
        print(f'{n} * {i} = {n*i}')

n = int(stdin.readline())
gugu(n)
