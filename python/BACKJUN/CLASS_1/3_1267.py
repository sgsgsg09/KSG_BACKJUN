"""동호는 새악대로 T 통신사의 새 핸드폰 옴머나를 샀다. 새악대로 T 통신사는 동호에게 다음 두 가지 요금제 중 하나를 선택하라고 했다.

영식 요금제
민식 요금제
영식 요금제는 30초마다 10원씩 청구된다. 이 말은 만약 29초 또는 그 보다 적은 시간 통화를 했으면 10원이 청구된다. 만약 30초부터 59초 사이로 통화를 했으면 20원이 청구된다.

민식 요금제는 60초마다 15원씩 청구된다. 이 말은 만약 59초 또는 그 보다 적은 시간 통화를 했으면 15원이 청구된다. 만약 60초부터 119초 사이로 통화를 했으면 30원이 청구된다.

동호가 저번 달에 새악대로 T 통신사를 이용할 때 통화 시간 목록이 주어지면 어느 요금제를 사용 하는 것이 저렴한지 출력하는 프로그램을 작성하시오."""

"""첫째 줄에 싼 요금제의 이름을 출력한다. 그 후에 공백을 사이에 두고 요금이 몇 원 나오는지 출력한다. 만약 두 요금제의 요금이 모두 같으면 영식을 먼저 쓰고 민식을 그 다음에 쓴다.

영식은 Y로, 민식은 M으로 출력한다."""




from sys import stdin
from typing import List
"""
def calculate_cost(N: int, base_time: int, base_cost: int):
    quotient = N // base_time
    remainder = N % base_time

    if remainder > 0:
        return (quotient + 1) * base_cost

    return quotient * base_cost

"""
def Y_T(N:int):
    quotient = N // 30
    remainder = N % 30

    if(remainder >= 0):
        return (quotient+1)*10

    return quotient*10


def M_T(N:int):
    quotient = N // 60
    remainder = N % 60

    if(remainder >= 0):
        return (quotient+1)*15

    return quotient*15

def add(*args: int):
    arg = sum(args)
    return arg

n = int(stdin.readline())
li = list(map(int, stdin.readline().split()))
lis = []
a=0
b=0
for i in range(n):
    # 값을 집어 넣어서 비교해야함.
    #영식은 영식끼리 민식은 민식끼리 해야함.
    a = a + Y_T(li[i])
    b = b + M_T(li[i])

if a < b:
    print(f"Y {a}")
elif a==b:
    print(f"Y M {a}")
else:
    print(f"M {b}")
    
    
