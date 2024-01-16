from sys import stdin

#black_jack
def black_jack(arg, args):
    max_val = arg[1]
    sort_args = sorted(args)
    # 1,2,3 의 수를 합하는 코드
    def find_black(arg, M):
        #1,3,5의 위치 일때는? 어떻게 할껴? 모든 경우를 다 탐색하나?
        #한 개를 잡고 이를 기준으로 범위를 나누자.
        closet_sum = 0
        for i in range(len(arg) - 1):
            left = i + 1
            right = len(arg) - 1

            while left < right:
                current_sum = arg[i] + arg[left] + arg[right]

                if current_sum <= M:
                    if abs(M - current_sum) < abs(M - closet_sum):
                        closet_sum = current_sum

                    left += 1
                else:
                    right -= 1
            
            # print(arg[i], arg[left], arg[right])
        return closet_sum
    a = find_black(sort_args, max_val)
    print(a)

lis = list(map(int,stdin.readline().split()))
lis_num = list(map(int, stdin.readline().split()))

black_jack(lis, lis_num)