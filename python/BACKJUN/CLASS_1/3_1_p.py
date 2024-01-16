from typing import List
#타입 힌팅(Type Hinting)을 위한 것입니다. 타입 힌팅은 파이썬 3.5 이후부터 도입된 기능으로, 변수, 함수 매개변수, 함수 반환 값 등에 대한 타입 정보를 제공하는 방법입니다. 이를 통해 코드의 가독성을 높이고 오류를 미리 방지하는데 도움을 줍니다
def minimum_distance(x: int, y: int, w: int, h: int) -> int:
    # 왼쪽 아래 꼭짓점부터의 거리와 오른쪽 위 꼭짓점부터의 거리를 계산
    distance_to_left = x
    distance_to_right = w - x
    distance_to_bottom = y
    distance_to_top = h - y
    
    # 각 방향으로의 거리 중 최솟값을 반환
    return min(distance_to_left, distance_to_right, distance_to_bottom, distance_to_top)

def main():
    # 입력 받기
    location_input = input("한수의 현재 위치 (x, y)와 직사각형의 오른쪽 위 꼭짓점 (w, h)를 공백으로 구분하여 입력하세요: ")
    location_input_list = location_input.split()
    location_input_list_number = [int(x) for x in location_input_list]
    
    # 최솟값 계산
    result = minimum_distance(*location_input_list_number)
    #이 문법은 리스트나 튜플의 원소들을 함수의 인자로 전달하는 방법 중 하나입니다. 인자로 전달하는 것이다!

    # 결과 출력
    print("최솟값:", result)

if __name__ == "__main__":
    main()
#if __name__ == "__main__":은 스크립트가 직접 실행될 때만 해당 코드 블록을 실행하도록 하는 역할을 합니다. 이것은 스크립트가 모듈로 사용될 때는 실행되지 않습니다.