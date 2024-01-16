from sys import stdin

#sort len, word
def sort_l_w(arg):
    # sort_dict = {item: len(item) for item in arg}
    sort_dict = {item: len(item) for item,item in enumerate(arg)}
    sort_lis = sorted(sort_dict.items(), key = lambda x : (x[1],x[0]))
    for i in range(len(sort_lis)):
        print(sort_lis[i][0])



n = int(stdin.readline().rstrip())
lis = []
for i in range(n):
    lis.append(stdin.readline().rstrip())

sort_l_w(lis)