from sys import stdin

#알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

#word location
def w_l(arg):
    start_alpha = ord('a')
    end_alpha = ord('z') +1
    alpha_lis = list(chr(i) for i in range(start_alpha, end_alpha))
    def dict(arg, arg_args):
        dict_alpha = {}
        s=''
        for char in arg:
            dict_alpha[char] = -1
            if char in arg_args:
                dict_alpha[char] = arg_args.index(char)
        s += ' '.join(str(i) for i in dict_alpha.values())
        return s
    print(dict(alpha_lis, arg))


lis = list(stdin.readline())
w_l(lis)