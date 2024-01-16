# 3번 하는 거야 N개의 정수가 주어지면, 이 정수들의 합 N개의 줄씩 S의 부호를 구하는 프로그램을 작성하시오.

# from sys import stdin
# n = int(stdin.readline())

# def process(N):
#     arr = []
#     N: int = int(input())
#     for i in range(N):
#         value = int(input())
#         arr.append(value)
#     #print(arr)
#     return judgement(*arr)

from typing import List
from sys import stdin
def process(set_number):
    N = int(stdin.readline())
    total = sum(int(stdin.readline()) for _ in range(N))
    return judgement(total)

def main():
    results = [process(set_number) for set_number in range(1,4)]

    # for set_number in range(1,4):
    #     result = process(set_number)
    #     results.append(result)
    
    for result in results:
        print(result)

def judgement(*args :int):
    arg = sum(args)
    if(arg == 0):
        return 0
    elif(arg < 0):
        return '-'
    return '+'


if __name__ == "__main__":
    main()
