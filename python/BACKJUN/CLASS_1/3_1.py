#한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

location_input = input()
location_input_list = location_input.split()

location_input_list_number = [int(x) for x in location_input_list]

def mini(location_input_list_number: list):
    a = comparision(abs(location_input_list_number[2] - location_input_list_number[0]),location_input_list_number[0])
    b = comparision(abs(location_input_list_number[1] - location_input_list_number[3]),location_input_list_number[1])
    mini_value = a if a <b else b
    return mini_value
def comparision(a:int, b:int):
    return abs(a if a<b else b)

print(mini(location_input_list_number))


