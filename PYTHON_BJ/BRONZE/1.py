#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오
# def f(a,b):
#     c = a + b
#     return c

# A = (input())
# A = (A.split())
# A = [int(x) for x in A]
# c1 = f(A[0], A[1])
# print(c1)

#sum 과 맵도 한 번 보기.
"""
map은 iterable의 각 항목에 주어진 함수를 적용하고 결과를 포함하는 새로운 iterable을 반환하는 내장 함수이다.
map(1,2)
1. iterable의 각 항목에 적용될 함수
2. 처리할 항목을 포함하는 iterable.
"""
print((map(int ,input().split())))