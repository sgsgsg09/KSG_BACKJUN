'''
다섯 개의 자연수가 있다. 이 수의 적어도 대부분의 배수는 위의 수 중 적어도 세 개로 나누어 지는 가장 작은 자연수이다.

서로 다른 다섯 개의 자연수가 주어질 때, 적어도 대부분의 배수를 출력하는 프로그램을 작성하시오.
'''
from sys import stdin
#수의 약수를 찾기.
def mutually_exclusive(n :int):
    lis_n = []
    for i in range(1, n//2 + 1):
        if n % i == 0:
            lis_n.append(i)
    lis_n.append(n)
    #print(lis_n)
    return lis_n

#최소 공배수 찾기.
def least_common_multiple(arg:list):
    #포함되었을 때, 포함되지 않았을 때.
    n = len(arg)
    k = 0
    keys = 0
    while (keys := keys) < 3:
        k += 1
        keys = 0
        for i in range(n):
            if k % arg[i] == 0:
                keys += 1
    print(k)
    
                    
# 1. 5개의 입력을 받아야 한다.
li_n = list(map(int, stdin.readline().split()))

least_common_multiple(li_n)

#print(li_n)


#적어도 세 개로 나누어 지는 가장 작은 자연수를 골라야 한다.
#그럼 적당히 큰 n을 잡은 다음에 이를 3개이상 만족 시키는것이 합리적인가?
#아니다 차라리 순환을 돌면서 최소 공배수를 찾고 이에 해당하는 나머지 숫자를 찾자
# 더 좋은 방식 각 숫자에 대한 공약수를 찾자. 이

    
#약수 찾기
def measure(arg:list):
    n = len(arg)

    arg_li = [[] for _ in range(n)]

    for i in range(n):
        arg_li[i] = mutually_exclusive(arg[i])
    return arg_li
