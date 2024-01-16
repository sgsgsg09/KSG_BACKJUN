a = 5
lis_n = [a]
print(lis_n)
while(a > 0):
    lis_n.insert(1,a % 10)
    a = a // 10