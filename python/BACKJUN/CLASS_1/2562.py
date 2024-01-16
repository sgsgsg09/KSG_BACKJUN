# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

# 예를 들어, 서로 다른 9개의 자연수

# 3, 29, 38, 12, 57, 74, 40, 85, 61

# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

from sys import stdin

def max_idx(arg):
    max_value = max(arg)
    max_index = arg.index(max_value)
    print(max_value)
    print(max_index + 1)

lis = []
for i in range(9):
    lis.append(int(stdin.readline()))

max_idx(lis)