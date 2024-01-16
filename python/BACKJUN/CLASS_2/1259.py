#pellim
from sys import stdin

#number of palindrome 
def no_pal(arg):
    n = len(arg) //  2
    if n == 0:
        n = 1
    bo : bool = False
    for i in range(n):
        if arg[i] != arg[-(i+1)]:
            bo = False
            break
        else:
            bo = True
    if bo == False:
        return 'no'
    else:
        return 'yes'


n = []
while(1):
    lis = list(stdin.readline().strip())
    if(lis[0] == '0'):
        break
    a = no_pal(lis)
    n.append(a)
for i in range(len(n)):
    print(n[i])