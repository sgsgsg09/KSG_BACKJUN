from sys import stdin

#greatest least common divisor
def great_di(arg):
    #uclid hoze
    def UC_HO(args):
        args = sorted(args, reverse=True)
        while(1):
            r = args[0] % args[1]
            if r == 0:
                return args[1]
            args[0] = args[1]
            args[1] = r
        
    print(UC_HO(arg))
    least = [int(x/UC_HO(arg)) for x in arg]
    sum_mul = least[0] * least[1] * UC_HO(arg)
    print(int(sum_mul))

lis = list(map(int, stdin.readline().split()))
great_di(lis)