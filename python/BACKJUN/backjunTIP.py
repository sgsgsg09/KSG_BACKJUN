from sys import stdin
n = int(stdin.readline())

# 입력받아야 할 것이 한 줄에 여러 개라면 input()보다 readline() 함수를 이용하는 것이 훨씬 더 빠르다.

li = list(map(int, stdin.readline().split()))

# 3 3
# 1 1 0
# 1 1 1
# 1 0 1
# 1 1 1
# 이 코드로 입력받을 수 있다.

n, m = list(map(int, stdin.readline().split()))
li = [] 
for i in range(n):
    li.append(list(map(int, stdin.readline().split())))


li = []
for i in range(n):
	li.append(int(sys.stdin.readline()))
      
# 그리고 출력할 때에 줄바꿈을 해야 한다면

for i in li:
	print(i)
# 이렇게 하는 것은 매우 비효율적이고

 

s = ""  
for i in li:
    s += (str(i) + '\n')
print(s)