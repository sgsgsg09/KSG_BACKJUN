'''
문제
어떤 수 X가 주어졌을 때, X의 모든 자리수가 역순이 된 수를 얻을 수 있다. Rev(X)를 X의 모든 자리수를 역순으로 만드는 함수라고 하자. 예를 들어, X=123일 때, Rev(X) = 321이다. 그리고, X=100일 때, Rev(X) = 1이다.

두 양의 정수 X와 Y가 주어졌을 때, Rev(Rev(X) + Rev(Y))를 구하는 프로그램을 작성하시오

[형식]
14 13 /15,85

1. 띄어쓰기로 구분된 값을 얻자.
2. rev 자릿수를 역순으로 만드는 함수를 만들자.
3. 이를 더하자. > 다시 rev에 집어 넣자.

2. 자릿수를 역순으로 만드는 방법
    1. string로 값을 분류한다음 reverse함수를 쓰자. [4,1] [3,1]/[5,1][5,8]
3. 더하는 방법. > rev
    zip함수 > [7,2]/[10,9]
    27 > 그냥 더하면 안됨? 100같은 0자릿수 땜에 안됨!


'''

from sys import stdin
from itertools import zip_longest

def rev(lis):
    arg,*args = lis
    
    def rev_num(li):
        rev_arg = [int(num) for num in reversed(list(str(li)))]

        return rev_arg
    
    rev_arg = rev_num(arg)
    rev_args = rev_num(args[0])

    rev_arg = digit_number(rev_arg)
    rev_args = digit_number(rev_args)

    rev_sum = rev_num(sum(rev_arg + rev_args))
    print(sum(digit_number(rev_sum)))

    

def digit_number(lis):

    lis = lis[::-1]

    lis = [number * pow(10,idx) for idx,number in enumerate(lis)]

    lis = lis[::-1]
    return lis



n = list(map(str,stdin.readline().split()))
rev(n)

