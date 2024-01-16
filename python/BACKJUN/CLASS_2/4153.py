from sys import stdin

#right triangle
def r_t(arg):
    arg = [x**2 for x in arg]
    max_t = max(arg)
    # max_t_i = arg.index(max_t)
    arg = [x for x in arg if x != max_t]
    if max_t == arg[0] + arg[1]:
        return 'right'
    return 'wrong'

lis_t = []
while True:
    lis = list(map(int, stdin.readline().split()))
    if all(x == 0 for x in lis):
        break
    
    lis_t.append(r_t(lis))
print('\n'.join(lis_t))
 