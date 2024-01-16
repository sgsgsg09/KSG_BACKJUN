from sys import stdin

#judgement major_scale
def judgement_m_s(arg):
    n = len(arg)
    result = 0
    for i in range(n):
        if i == 7:
            break
        result = arg[i+1] - arg[i]
        if abs(result) > 1:
            print("mixed")
            break
    if result == 1:
        print("ascending")
    elif result == -1:
        print("descending")

lis = list(map(int, stdin.readline().split()))
judgement_m_s(lis)
