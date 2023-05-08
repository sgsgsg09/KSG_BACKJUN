# 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.
def minus(a):
    return a[0] - a[1]
print(minus(list(map(int ,input().split()))))
#map함수는 레퍼런스에 대한 주소를 가지고 있음.
