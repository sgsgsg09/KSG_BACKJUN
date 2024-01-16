from sys import stdin
import math
#disassemble
def disassemble(dis_n):
    # dis_n == a + a[1,2,3,....]
    
    def new_number(dis_num):
        # num_digit = int(math.log10(dis_num))
        # dis_n = 10**num_digit - 10*num_digit
        dis_n = 0
        while(1):
            dis_n = dis_n + 1
            a = dis_n
            lis_n = [a]
            while(a > 0):
                lis_n.insert(1,a % 10)
                a = a // 10
            if(dis_num == sum(lis_n)):
                return lis_n[0]

            if(dis_n > dis_num):
                return 0

    a = new_number(dis_n)
    print(a)


dis_n = int(stdin.readline().rstrip())
disassemble(dis_n)