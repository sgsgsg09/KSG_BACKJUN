from sys import stdin

#chess_map
def chess(arg, width):
    #text
    #8x8범위 내에서 x,y위치에 해당하는 체스판 알아야 함.
    def color_check(arg_col, depth):
        chess_lis = ['B', 'W']
        x= 0
        y= 0
        arg_error = []
        # x,y로 써 값을 판단하기.
        #검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다
        # x,y != (x+1,y),(x,y+1)
        print(len(arg_col[0]) - 1)
        for x in range(len(arg_col[1])- 1):
            for y in range(len(arg_col[0]) - 1):
                if arg_col[x][y] == arg_col[x][y+1]:
                    if arg_col[x][y] == 'B':
                        arg_col[x][y+1] = 'W'
                    else:
                        arg_col[x][y+1] = 'B'
                    arg_error.append([x,y+1])
                    
                if arg_col[x][y] == arg_col[x+1][y]:
                    if arg_col[x][y] == 'B':
                        arg_col[x+1][y] = 'W'
                    else:
                        arg_col[x+1][y] = 'B'
                    arg_error.append([x+1,y])
        return arg_error
    a = color_check(arg, width)
    return a
lis = list(map(int, stdin.readline().split()))
lis_chess = []

for i in range(lis[0]):
    lis_chess.append(list(stdin.readline().strip()))
print(chess(lis_chess,lis[1]))