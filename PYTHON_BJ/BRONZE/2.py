# 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.
def minus(a):
    return a[0] - a[1]
print(minus(list(map(int ,input().split()))))
#map함수는 레퍼런스에 대한 주소를 가지고 있음.

#A,B = map(int,input().split())
"""
unpacking syntax는 시퀀스(목록, 튜플 또는 맵 개체)에서 값을 추출하여 개별 변수에 할당하는 방법이다.
"""