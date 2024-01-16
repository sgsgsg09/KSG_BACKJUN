from sys import stdin

# divide 42
def d_42(arg):
    lis_42 = []
    #dict
    dict_42 = {}
    for i in range(len(arg)):
        lis_42.append(arg[i] % 42)
    for num in lis_42:
        if num in dict_42:
            dict_42[num] += 1
        else:
            dict_42[num] =1
    print(len(dict_42))

lis = []
for i in range(10):
    lis.append(int(stdin.readline()))
d_42(lis)