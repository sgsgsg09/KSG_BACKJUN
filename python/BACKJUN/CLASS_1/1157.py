#첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

from sys import stdin

def count(arg:str):
    char_count = {}
    for char in arg:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return select(char_count)

def select(arg):
    max_count = max(arg.values())
    #max_count를 기반해서 keys를 찾아야 함.
    max_chars = [key for key,value in arg.items() if max_count == value]
    return [max_chars, max_count]

coffee = stdin.readline().upper().strip()


max_word =count(coffee)

if len(max_word[0]) > 1:
    print("?")
else:
    print(max_word[0][0])
    
