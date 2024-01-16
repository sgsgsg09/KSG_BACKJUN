from sys import stdin

def verification(arg):
    arg = [x**2 for x in arg]
    total = sum(arg)
    totao_d = total % 10
    return totao_d

li = list(map(int, stdin.readline().split()))

print(verification(li))